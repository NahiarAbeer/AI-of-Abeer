import speech_recognition as sr
import pyttsx3 as tts
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import subprocess


listener = sr.Recognizer()
guddu = tts.init()
# voices = guddu.getProperty('voices')
# # guddu.setProperty('voice',voices[1].id)


def talk(text):
    guddu.say(text)
    guddu.runAndWait()


def take_command():
    talk('How can i help you')
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'guddu' in command:
                command=command.replace('guddu','')
                # print(command)

                return command
    except Exception as e:

        print(e)    

        print("Unable to Recognize your voice.")  

        return "None"
        


def runguddu():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('its'+time)
    elif 'date' in command:
        date=datetime.datetime.now().strftime('%d %B %A')
        talk(date)
        print(date)
    elif 'play' in command:
        content= command.replace('play','')
        talk(f'playing this {content} sir')
        pywhatkit.playonyt(content)
    elif 'tell me about' in command:
        lookFor=command.replace('tell me about','')
        info=wikipedia.summary(lookFor,1)
        talk(info)
    elif 'thank' in command:
        talk('welcome')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'search about' in command:
        command=command.replace('search','')
        pywhatkit.search(command)
    elif 'facebook' in command:
        talk('wait')
        webbrowser.open('https://www.facebook.com/')
        talk('Here\'s your data')
    elif 'chat gpt' in command:
        webbrowser.open('https://chat.openai.com/chat')  
    elif 'spotify' in command:
        subprocess.Popen('spotify.exe')      
    else :
        talk('try again sir')    

for i in range(5):
    runguddu()
