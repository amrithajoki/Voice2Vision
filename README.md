# Voice2Vision
Voice2Vision is an AI-powered, voice-controlled accessibility tool designed to assist visually impaired users  describing the content of their environment using real-time camera capture and provides a descriptive response powered by Groq’s multimodal LLaMA model.
🔧 TECHNOLOGIES USED:


AI / Machine Learning
Groq API (GPT-4 Vision via LLaMA 4 model)
Used to analyze images and return a textual description of the scene for the visually impaired.

🗣️ Voice Interaction
SpeechRecognition (Python library)
Converts voice commands into text (e.g., detecting "capture" and taking user prompts).

pyttsx3 (Text-to-Speech)
Converts the generated description into audio output for the user.

📷 Computer Vision
OpenCV (cv2)
Captures images from the device's camera and encodes them in memory (Base64 format) for Groq.

📦 API Handling
Requests (Python)
Sends the image and prompt data to Groq’s API and handles the response.

📲 User Interface (Frontend)
Kivy (Python GUI framework)
Provides a simple, touch-friendly UI with a mic button and voice-activated interaction.

Kivy Properties & Layouts (e.g., BoxLayout, Label, Image)
Used to structure the screen and interface elements.

🔐 Configuration & Environment Management
python-dotenv
Loads the Groq API key securely from a .env file.

📱 Mobile Deployment

Buildozer
Packages the app for Android using Python files, Kivy interface, and all dependencies.

🗣️ VOICE CONTROL IMPLEMENTATION


Wake word: “capture”
The microphone is always listening using the speech_recognition library.
Once “capture” is heard:
The app captures an image using the webcam.
It prompts the user to ask a question using voice.
The voice prompt + image is sent to the Groq API for intelligent response generation.
The response is read aloud using pyttsx3.

🌐 BACKEND INTELLIGENCE:


The Groq API (LLaMA 4 Scout) receives a voice-based question and an image in base64 format.
It responds with a short, casual, blind-friendly description.
Example Prompt: "In a short and casual way, answer this question based on the image for a blind person: What’s happening here?"

📱 FRONTEND (UI with Kivy)

A minimal and accessible UI with:

A mic icon (to start voice interaction)

A status label

Background color for visual clarity

Tap the mic icon to trigger the backend process (in mobile or desktop environments).

📦 HOW TO RUN THE PROJECT:


Step 1: Install the Required Libraries
Install all required Python libraries from requirements.txt.

Step 2: Set Up Your Environment
Create a .env file to securely load your Groq API key.

Step 3: Run the Backend
Start the backend by running the Python script that handles the voice command, image capture, and interaction with the Groq API.

Step 4: Run the Frontend
Launch the Kivy app to interact with the user interface.

Step 5: Package the App (For Mobile)
Use Buildozer to package the app for Android deployment.

Run the buildozer command to compile the app for Android.

🚀 FUTURE ENHANCEMENTS:

Add multilingual support (Tamil, Hindi, etc.)

Integrate offline fallback using on-device models

Add scene memory and summaries for low-vision users

Develop a hardware-integrated model with physical button access



