from datetime import datetime
from email import contentmanager
from email.mime import audio
from http import server
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how may i help you")
def take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 0.8
        r.energy_threshold = 4000
        
        audio=r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")      
    except Exception as e:
         
        print("say that again please.... ")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your password-here')
    server.sendmail('yuremail@gmail.com',to,content)
    server.close()
    

if __name__ == "__main__":
    wishMe()
    while True:
        query=take_Command().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia.......")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open chrome' in query:
            webbrowser.open('chrome.com')

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir= 'E:\\music_dir'
            songs = os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'email to peeyush' in query:
            try:
                speak("what should i say!")
                content = take_Command()
                to = "youremail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend , i am not able to send this mail")

        elif 'quit' in query:
           
            speak('ok sir')
            exit()


        