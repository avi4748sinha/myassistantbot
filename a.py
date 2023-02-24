import speech_recognition as sr
import pyttsx3
import requests
import json
import webbrowser
import pywhatkit
import wikipedia
import datetime
import os

# create a text-to-speech engine
engine = pyttsx3.init()

# define the voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # set the voice to female

# define the listening function
def listen():
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
        print(e)
        print("Please say that again...")
        return "None"
    return query.lower()

# define the speaking function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define the main function
def main():
    speak("Hello, Avi. I am your assistant how can i assist you?")

    while True:
        query = listen()

        # command to exit the program
        if "exit" in query:
            speak("Goodbye!")
            break

        # command to search the internet
        elif "search for" in query:
            query = query.replace("search for", "")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get().open(url)
            speak(f"Here are the results for {query} on Google.")

        # command to open a website
        elif "open" in query:
            query = query.replace("open", "")
            url = f"https://www.{query}.com"
            webbrowser.get().open(url)
            speak(f"Opening {query} website.")

        # command to play a song on YouTube
        elif "play" in query:
            query = query.replace("play", "")
            pywhatkit.playonyt(query)
            speak(f"Playing {query} on YouTube.")

        # command to get information from Wikipedia
        elif "who is" in query or "what is" in query:
            query = query.replace("who is", "")
            query = query.replace("what is", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        # command to do mathematical calculations
        elif "calculate" in query:
            query = query.replace("calculate", "")
            result = str(eval(query))
            speak(f"The answer is {result}.")

        # command to send a WhatsApp message
        elif "send message" in query:
            query = query.replace("send message to", "")
            number = "+919504919122" # replace with your own WhatsApp number
            message = query
            pywhatkit.sendwhatmsg(number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
            speak("Message sent successfully.")

        # command to remember data
        elif "remember" in query:
            data = query.replace("remember", "")
            with open("data.txt", "w") as f:
                f.write(data)
            speak("Data saved successfully.")

        # command to recall data
        elif "recall" in query:
            with open("data.txt", "r") as f:
                data = f.read()
            speak(f"The data you asked me to remember is {data}.")

# run the main function
if __name__ == '__main__':
    main()
