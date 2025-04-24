[app]

title = Voice2Vision
package.name = voice2vision
package.domain = org.example
source.dir = .
source.include_exts = py,png,kv,txt
version = 1.0
requirements = python3,kivy,opencv-python,pyttsx3,speechrecognition,requests,python-dotenv
orientation = portrait
fullscreen = 1
source.main = main.py

# Icon (optional)
# icon.filename = icon.png

[buildozer]

log_level = 2
warn_on_root = 1

[app.android]

# Permissions required by your app
android.permissions = CAMERA, RECORD_AUDIO, INTERNET

# Android-specific requirements
android.api = 33
android.minapi = 24
android.ndk = 25b
android.arch = arm64-v8a
android.allow_clear_user_data = 1

# Support for speech recognition and microphone
android.useandroidnativeaudio = 1

# Allow external APIs like Groq
android.internet = 1

# To avoid audio or OpenCV crashing, set SDL
android.entrypoint = org.kivy.android.PythonActivity
android.enable_androidx = 1

# If using camera
android.hardware = camera

# Optional: force OpenCV compatibility
android.meta_data = android.hardware.camera, android.hardware.camera.autofocus

[app.android.ndk]
# Recommended for OpenCV
android.ndk_path = 

[app.android.p4a_args]
# To speed up build
# --private works only on debug mode