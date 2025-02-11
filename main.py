import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import client
# import client from client.py

ttsx = pyttsx3.init()
voices = ttsx.getProperty('voices')
# print(voices)
#engine.setProperty('voice', voices[0].id) 
ttsx.setProperty('voice', voices[1].id)

def speak(command):
    ttsx.say(command)
    ttsx.runAndWait()

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open github" in command.lower():
        webbrowser.open("https://www.github.com")

    else:
        #let AI handle the command
        response = client.generate_text(command)
        speak(response)



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r= sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout =4 )
            word = r.recognize_google(audio)
            print("You said: {}".format(word))
            if "jarvis" in word.lower():
                speak("Yes?")
                print("JArvis is Active...")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command)
                processCommand(command)
        except Exception as e:
            print(e , "Sorry, I did not get that. Please repeat.")
            # speak("Sorry, I did not get that. Please repeat.")