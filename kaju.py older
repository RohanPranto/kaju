# built-in modules.
import datetime
import os  # open any local app
import webbrowser

# third-party imports
import fontstyle
import pyjokes
import pyttsx3
import pywhatkit  # to play music or any other media files
import requests  # request result from online
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
# to set to female voice, uncommand next two lines
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def talk(text: str) -> None:
    engine.say(text)  # engine.say('whats up human, how can i help you')
    engine.runAndWait()


def take_command() -> str:
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('how can i help you?')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass

    return command


def run_assistant() -> None:
    command: str = take_command()
    print(command)

    match command:
        case 'play':
            song = command.replace('play', '')
            talk('playing ' + song)
            print(fontstyle.apply('playing', 'bold/Italic/red/UNDERLINE/GREEN_BG'))
            pywhatkit.playonyt(song)

        case 'time':
            time = datetime.datetime.now().strftime('%I %M %p')
            timetext = fontstyle.apply(time, 'bold/Italic/red/GREEN_BG')
            print(timetext)
            talk('its' + time)

        case 'who is':
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            infotext = fontstyle.apply(info, 'bold/Italic/red/GREEN_BG')
            print(infotext)
            talk(info)

        case 'what is':
            person = command.replace('what is', '')
            info = wikipedia.summary(person, 1)
            infotext = fontstyle.apply(info, 'bold/Italic/red/GREEN_BG')
            print(infotext)
            talk(info)

        case 'single':
            printsingle = fontstyle.apply(
                'Sorry I am already in a relationship with wifi',
                'bold/Italic/red/GREEN_BG',
            )
            print(printsingle)
            talk('Sorry I am already in a relationship with wifi')

        case 'joke':
            jokes = pyjokes.get_joke()
            joketext = fontstyle.apply(jokes, 'bold/Italic/red/GREEN_BG')
            print(joketext)
            talk(jokes)

        case 'open youtube':
            webbrowser.open("youtube.com")
            talk('opening')
            print(fontstyle.apply('Opening', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

        case 'open google':
            webbrowser.open("google.com")
            talk('opening')
            print(fontstyle.apply('Opening', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

        case 'open facebook':
            webbrowser.open("facebook.com")
            talk('opening')
            print(fontstyle.apply('Opening', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

        case 'open instagram':
            webbrowser.open("instagram.com")
            talk('opening')
            print(fontstyle.apply('Opening', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

        case 'open browser':
            CodePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(CodePath)
            print(fontstyle.apply('Opening', 'bold/Italic/red/UNDERLINE/GREEN_BG'))
            talk('opening')

        case 'weather':
            search = "temperature"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            print(
                fontstyle.apply(
                    'Current Temperature is', 'bold/Italic/red/UNDERLINE/GREEN_BG'
                )
            )
            weathertext = fontstyle.apply(temp, 'bold/Italic/red/GREEN_BG')
            print(weathertext)
            talk(f"current temperature is {temp}")

        case 'thank you':
            talk('See You Again!')
            print(
                fontstyle.apply('See You Again', 'bold/Italic/yellow/UNDERLINE/RED_BG')
            )
            exit(run_assistant)

        case _:
            talk('Sorry, Can you repeat?')


while True:
    run_assistant()
