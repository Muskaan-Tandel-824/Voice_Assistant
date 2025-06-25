import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import random
import subprocess
import ctypes
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user's voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            return query.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "There was an issue connecting to the speech recognition service."
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your assistant, ALLEN.")

def main():
    """Main function to run the voice assistant."""
    speak(" How can I help you today?")
    while True: 
        query = listen()
        print(f"You said: {query}")
        if "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a great day!")
            break
        elif "hello" in query:
            speak("Hello! How can I assist you?")
        elif "your name" in query:
            speak("I am your voice assistant ALLEN.")
        elif "time" in query:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\MUSKAN\\Music"
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("Music folder not found.")
        elif 'shutdown' in query:
            speak("Shutting down the system.")
            subprocess.call('shutdown /s /t 5')

        elif 'lock window' in query:
            ctypes.windll.user32.LockWorkStation()

        elif 'restart' in query:
            speak("Restarting the system.")
            subprocess.call('shutdown /r /t 5')


        else:
            speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    wishMe()
    main()
    