# Importing the necessary modules and libraries
import datetime
import os
import webbrowser
import fontstyle
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup

# Initialize the speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize and process user commands
def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('Listening...')
            talk('How can I help you?')
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        command = ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        command = ""
    return command


# Main function to run the virtual assistant
def run_assistant():
    command = take_command()
    print(command)

    if command.startswith('play'):
        # Extract the song name from the command
        song = command.replace('play', '').strip()
        if song:
            talk('Playing ' + song)
            print(fontstyle.apply('Playing', 'bold/Italic/red/UNDERLINE/GREEN_BG'))
            pywhatkit.playonyt(song)
        else:
            talk('Please specify a song name.')

    elif command == 'time' or command=="tell me the time":
        time = datetime.datetime.now().strftime('%I:%M %p')
        timetext = fontstyle.apply(time, 'bold/Italic/red/GREEN_BG')
        print(timetext)
        talk('It\'s ' + time)
    
    elif command == 'date' or command == 'tell me the date':
       date = datetime.date.today().strftime('%B %d, %Y')
       datetext = fontstyle.apply(date, 'bold/Italic/red/GREEN_BG')
       print(datetext)
       talk('Today\'s date is ' + date)

    elif command.startswith('who is'):
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        infotext = fontstyle.apply(info, 'bold/Italic/red/GREEN_BG')
        print(infotext)
        talk(info)

    elif command.startswith('what is'):
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        infotext = fontstyle.apply(info, 'bold/Italic/red/GREEN_BG')
        print(infotext)
        talk(info)

    elif command == "single" or command=="are you single":
        printsingle = fontstyle.apply(
            'Sorry, I am already in a relationship with Wi-Fi',
            'bold/Italic/red/GREEN_BG',
        )
        print(printsingle)
        talk('Sorry, I am already in a relationship with Wi-Fi')

    elif command == 'joke' or command == "tell me a joke":  # Recognize both "joke" and "tell me a joke"
        joke = pyjokes.get_joke()
        joketext = fontstyle.apply(joke, 'bold/Italic/red/GREEN_BG')
        print(joketext)
        talk(joke)

    elif command == 'open youtube':
        webbrowser.open('https://www.youtube.com')
        talk('Opening YouTube')
        print(fontstyle.apply('Opening YouTube', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif command == 'open google':
        webbrowser.open('https://www.google.com')
        talk('Opening Google')
        print(fontstyle.apply('Opening Google', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif command == 'open facebook':
        webbrowser.open('https://www.facebook.com')
        talk('Opening Facebook')
        print(fontstyle.apply('Opening Facebook', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif command == 'open instagram':
        webbrowser.open('https://www.instagram.com')
        talk('Opening Instagram')
        print(fontstyle.apply('Opening Instagram', 'bold/Italic/red/UNDERLINE/GREEN_BG'))

    elif command == 'open browser':
        CodePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(CodePath)
        print(fontstyle.apply('Opening Browser', 'bold/Italic/red/UNDERLINE/GREEN_BG'))
        talk('Opening Browser')

    elif command == 'weather' or "Tell me the weather":
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
        talk(f"Current temperature is {temp}")

    elif command == 'thank you' or command=="bye bye":
        talk('See you again!')
        print(
            fontstyle.apply('See you again', 'bold/Italic/yellow/UNDERLINE/RED_BG')
        )
        exit()

    else:
        talk('Sorry, can you repeat that?')

# Main loop to continuously listen for user input
while True:
    run_assistant()
