import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess as sp
import os
import random
import cv2

listener = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takecommand(ask=""):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        talk('Listening')
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing")
            talk("Recognizing")
            command = r.recognize_google(audio, language='en-in')
            print(command)
        except Exception as e:
            print(e)
            print("Say that again please")
            talk("say that again please")
            return ""
        return command.lower()

def askname():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("what is your name")
        talk('what is your name')
        speak = r.listen(source)
    try:
        name = r.recognize_google(speak, language='en-in')
        l = ["Sravani","Reddy","Gudibandi"]
        lname = list(name.split())
        for i in lname:
            if i.lower() in l:
                hour = int(datetime.datetime.now().hour)
                greeting = "good morning" if hour < 12 else "good afternoon" if hour < 18 else "good evening"
                print(f"{greeting} {i}")
                talk(f"{greeting} {i}")
                print('what can i do for you')
                talk('what can i do for you')
                return
        print("incorrect name")
        talk("incorrect name")
        quit()
    except Exception as e:
        print("Say that again please...")
        talk("Say that again please")
        askname()

def main():
    while True:
        command = takecommand()
        if not command:
            continue
        print(command)
        
        # youtube video
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        
        # your name
        elif 'your name' in command:
            print('my name is AI')
            talk('my name is AI')
        
        # time
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)
        
        # wikipedia
        elif 'definition of' in command:
            try:
                _, _, person = command.split(' ', 2)
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except Exception as e:
                print(e)
                print('sorry could not find information')
                talk('sorry could not find information')
        
        # random music
        elif 'music' in command:
            music_dir = "C:\\Users"
            files = os.listdir(music_dir)
            music = random.choice(files)
            os.startfile(os.path.join(music_dir, music))
        
        # day
        elif 'day' in command:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
            if day in Day_dict:
                dayw = Day_dict[day]
                print(dayw)
                talk("The day is " + dayw)
        
        # spotify song
        elif 'song' in command:
            search = command.replace('song', '')
            url = "https://open.spotify.com/search/" + search
            webbrowser.get().open(url)
            talk("You are listening to " + search + " enjoy mam")
        
        # how are you
        elif 'how are you' in command:
            print('I am fine')
            talk('I am fine')
        
        # weather
        elif "weather" in command:
            url = "https://www.google.com/search?q=weather"
            webbrowser.get().open(url)
            talk("Here is what I found on google")
        
        # joke
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        
        # notepad
        elif 'notepad' in command:
            print('opening notepad')
            talk('opening notepad')
            sp.call("Notepad.exe")
        
        # calculator
        elif 'calculator' in command:
            print('opening calculator')
            talk('opening calculator')
            sp.call("calc.exe")
        
        # command prompt
        elif 'command prompt' in command:
            print('opening command prompt')
            talk('opening command prompt')
            sp.call("cmd.exe")
        
        # search for anything
        elif "search" in command:
            try:
                search_query = command.replace('search', '')
                pywhatkit.search(search_query)
                print("Searching")
                talk("searching " + search_query)
            except Exception as e:
                print(e)
                print("sorry, unable to find the information")
                talk("sorry, unable to find the information")
        
        # open any website
        elif 'open' in command:
            try:
                _, site = command.split(' ', 1)
                print('opening', site)
                talk('opening ' + site)
                webbrowser.open("http://www." + site + ".com")
            except Exception as e:
                print(e)
                print('Could not open the website')
                talk('Could not open the website')
        
        # whatsapp
        elif 'whatsapp' in command:
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().strftime('%M'))
            pywhatkit.sendwhatmsg('+918790208211', 'hai', hour, minute + 1)
        
        # exit
        elif 'exit' in command or 'stop' in command or 'quit' in command:
            print("Exiting...")
            talk("Exiting...")
            break
        
        else:
            talk('Please say the command again.')

print('hi i am AI your desktop assistant')
talk('hi i am AI your desktop assistant')
#askname()
main()

