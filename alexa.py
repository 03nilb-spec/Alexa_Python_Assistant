import speech_recognition as sr
import pyttsx3
from datetime import date
import pywhatkit as pw
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.say("I am Alexa")
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening.....")
        voice=listener.listen(source)
        command=listener.recognize_google(voices)
        command=command.lower()
        if 'alexa' in command:
            command=command.replace('alexa','')
            print(command)
    return command
def run_alexa():
    cmd=take_command()
    if 'play' in cmd:
        song=cmd.replace('play','')
        talk('playing'+song)
        #print('playing')
        #print('song')
        pw.playonyt(song)
    elif 'date' in cmd:
        today=date.today()
        print(today)
        talk('Today is' +today.strftime('%B %d, %Y'))
    elif 'time' in cmd:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is'+ time)
    elif 'prime minister' in cmd:
        #person=cmd.replace('who is the prime minister of india','')
        info=wikipedia.summary(cmd)
        print(info)
        talk(info)
    elif 'joke' in cmd:
        joking=pyjokes.get_joke(language='en',category='neutral')
        print(joking)
        talk(joking)
    elif 'are you single' in cmd:
        talk('I am in a relationship with wifi')
    else:
        talk('please say the command again')

while True:
    run_alexa()