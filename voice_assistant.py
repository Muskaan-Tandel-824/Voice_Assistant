import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon Dude!")
    else:
        speak("Good evening!")
    speak("How can I help you today My Dear?")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
    except:
        speak("Sorry, I didn't Understand.")
        return ""
    return command.lower()

def main():
    greet()
    while True:
        command = listen()

        if 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Current time is {current_time}")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")


        elif 'stop' in command or 'exit' in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command != "":
            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
 main()