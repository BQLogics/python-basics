import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def open_chrome():
    a = 'Opening Chrome..'
    speak(a)
    programName = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    subprocess.Popen([programName])

def get_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    print(current_time)
    speak(current_time)

def play_youtube(query):
    a = 'Opening YouTube..'
    speak(a)
    pywhatkit.playonyt(query)

def search_wikipedia(query):
    try:
        wikisearch = wikipedia.summary(query)
        print("Assistant:", wikisearch)
        speak(wikisearch)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Assistant: There are multiple options for your query. Please be more specific.")
        speak("There are multiple options for your query. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        print("Assistant: Sorry, I couldn't find any relevant information.")
        speak("Sorry, I couldn't find any relevant information.")
    except Exception as e:
        print("Assistant: An error occurred while processing your request.")
        speak("An error occurred while processing your request.")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def voice_assistant():
    with sr.Microphone() as source:
        print("Clearing background noises... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Ask me anything..')
        recordedaudio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message:', text)

        if 'chrome' in text:
            open_chrome()
        elif 'time' in text:
            get_time()
        elif 'play' in text:
            play_youtube(text)
        elif 'youtube' in text:
            webbrowser.open('www.youtube.com')
        else:
            search_wikipedia(text)

    except Exception as ex:
        print(ex)

while True:
    voice_assistant()