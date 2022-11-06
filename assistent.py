import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = speech.Recognizer() #it recognize the words and initialize in listener
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with speech.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:#if alexa is present in the sentence then it ask you to give command again 
                command = command.replace('alexa', '')
                print(command)
            elif 'siri' in command:#if siri is present in the sentence then it ask you to give command again 
                command = command.replace('siri', '')
                print(command)
    except:
        pass
    return command


def run_assistent():
    command = take_command()
    print(command)
    if 'play' in command:#few keywords to get certain usefull result
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        information = command.replace('searching', '')
        info = wikipedia.summary(information, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        information = command.replace('searching', '')
        info = wikipedia.summary(information, 1)
        print(info)
        talk(info)
    elif 'how to' in command:
        information = command.replace('searching', '')
        info = wikipedia.summary(information, 1)
        print(info)
        talk(info)
    else:
        talk('Please say the command again.')
    

while True:#if while is true the process continues
    run_assistent()
    
