import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text-to-speech function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greeting function
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you?")

# Speech-to-text function
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't get that. Can you please repeat?")
        return "None"
    return query

# Main function
if __name__ == "__main__":
    greet()
    while True:
        query = take_command().lower()

        # Open websites
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        # Play music
        elif 'play music' in query:
            music_dir = 'C:\\Music\\'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            speak("Playing music")

        # Get current time
        elif 'what time is it' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        # Exit program
        elif 'bye' in query:
            speak("Goodbye!")
            exit()
