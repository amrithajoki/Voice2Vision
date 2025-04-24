import cv2
import time
import base64
import requests
import os
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv

# Load the API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("🎙 Listening for wake word 'capture'...")
    speak("Listening for wake word capture")
    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                phrase = recognizer.recognize_google(audio).lower()
                print("🔊 Heard:", phrase)  # Add this for debugging
                if "capture" in phrase:
                    print("👂 Wake word 'capture' detected!")
                    speak("Yes, I am listening")
                    return
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("❌ Speech Recognition service error")
                break


def get_voice_prompt():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎤 Please ask your question...")
        speak("Please ask your question")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        prompt = recognizer.recognize_google(audio)
        print("🗣 Prompt received:", prompt)
        return prompt
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return "Describe the scene."
    except sr.RequestError:
        print("❌ Speech Recognition error")
        return "Describe the scene."

def run_voice2vision():
    listen_for_wake_word()

    print("📸 Capturing image for 3 seconds...")
    speak("Capturing image for 3 seconds")

    cam = cv2.VideoCapture(0)
    start_time = time.time()
    captured_frame = None

    while True:
        ret, frame = cam.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        cv2.imshow("Capturing...", frame)

        if time.time() - start_time > 3:
            captured_frame = frame
            break

        if cv2.waitKey(1) == 27:
            print("🚪 Escape pressed. Exiting...")
            break

    cam.release()
    cv2.destroyAllWindows()

    if captured_frame is not None:
        # Encode image directly from memory (no saving to file)
        _, buffer = cv2.imencode('.jpg', captured_frame)
        encoded_image = base64.b64encode(buffer).decode('utf-8')
        print("📸 Image captured and encoded in memory.")


        prompt_text = get_voice_prompt()

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"In a short and casual way, answer this question based on the image for a blind person: {prompt_text}"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                    ]
                }
            ],
            "max_tokens": 1000
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        print("📦 Groq API raw result:\n", result)

        if "choices" in result:
            description = result["choices"][0]["message"]["content"]
            print("\n🧠 Final Description:\n", description)
            speak(description)
            with open("result.txt", "w") as f:
                f.write(description)
            return description
        else:
            error_msg = "Unable to describe image."
            print("❌ Error from Groq API:\n", result)
            speak(error_msg)
            return error_msg
    else:
        speak("No image captured")
        return "No image captured."