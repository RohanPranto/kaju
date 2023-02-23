import speech_recognition as sr
import pyttsx3
import pywhatkit #to play music or any other media files
import datetime
import wikipedia
import pyjokes
import webbrowser
import os #open any local app
import requests #request result from online
from bs4 import BeautifulSoup
import fontstyle

listener = sr.Recognizer()
engine = pyttsx3.init()
# to set to female voice, uncommand next two lines
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def talk(text):
    # engine.say('whats up human, how can i help you')
    engine.say(text)
    engine.runAndWait()

def take_command():
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

def run_assistant():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(fontstyle.apply('playing',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p' )
        timetext = fontstyle.apply(time, 'bold/Italic/red/GREEN_BG')
        print(timetext)
        talk('its' + time)

    elif 'who is' in command:
      person= command.replace('who is' ,'')
      info= wikipedia.summary(person,1)
      infotext = fontstyle.apply(info, 'bold/Italic/red/GREEN_BG')
      print(infotext)
      talk(info)
      

    elif 'what is' in command:
      person= command.replace('what is' ,'')
      info= wikipedia.summary(person,1)
      infotext = fontstyle.apply(info, 'bold/Italic/red/GREEN_BG')
      print(infotext)
      talk(info)

    elif 'single' in command:
        
        printsingle=fontstyle.apply('Sorry I am already in a relationship with wifi', 'bold/Italic/red/GREEN_BG')
        print(printsingle)
        talk('Sorry I am already in a relationship with wifi')

    elif 'joke' in command:
        jokes=pyjokes.get_joke()
        joketext = fontstyle.apply(jokes, 'bold/Italic/red/GREEN_BG')
        print(joketext)
        talk(jokes)

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
        talk('opening')
        print(fontstyle.apply('Opening',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif 'open google' in command:
        webbrowser.open("google.com")
        talk('opening')
        print(fontstyle.apply('Opening',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif 'open facebook' in command:
        webbrowser.open("facebook.com")
        talk('opening')
        print(fontstyle.apply('Opening',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif 'open instagram' in command:
        webbrowser.open("instagram.com")
        talk('opening')
        print(fontstyle.apply('Opening',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif 'open browser' in command:
        CodePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(CodePath)
        print(fontstyle.apply('Opening',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))
        talk('opening')

    elif 'weather' in command:
        search = "temperature"
        url=f"https://www.google.com/search?q={search}"
        r= requests.get(url)
        data= BeautifulSoup(r.text,"html.parser")
        temp=data.find("div",class_="BNeawe").text
        print(fontstyle.apply('Current Temperature is',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))
        weathertext=fontstyle.apply(temp, 'bold/Italic/red/GREEN_BG')
        print(weathertext)
        talk(f"current temperature is {temp}")

    elif 'thank you' in command:
        talk('See You Again!')
        print(fontstyle.apply('See You Again',
                      'bold/Italic/yellow/UNDERLINE/RED_BG'))
        exit(run_assistant)

    else:
        talk('Sorry, Can you repeat?')

while True:
    run_assistant()


# pip install SpeechRecognition
# pip install pyttsx3
# pip install pywhatkit
# pip install wikipedia
# pip install pyjokes
# pip install requests
# pip install fontstyle
# pip install beautifulsoup4