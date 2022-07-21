import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!!!")
    elif hour>=16 and hour<20:
        speak("Good Evening!!!")
    else:
        speak("Good Night!!!")


def takeCommand():
    #audio to string
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anooplavangam17@gmail.com', 'fnhdkknzmkffwguv')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #takeCommand()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)

        elif 'send email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "buradaakhil@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry unable to send this email")    


        elif 'post email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vivekshonti3@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry unable to send this email")



