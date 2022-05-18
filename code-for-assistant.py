import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
from selenium import webdriver
from getpass import getpass

#print("Initializing OSIS")
MASTER = "Vivek"

engine = pyttsx3.init() # here we initialize pyttsx3 in a variable called engine
voices = engine.getProperty('voices') # here we assigned engine a voice 
engine.setProperty('voice', voices[0].id) # here we set the voice character ( 0 for male and 1 for female)
#engine.setProperty('rate', 180)

#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    print("OSIS : " + text)
    engine.runAndWait()

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning " + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon " + MASTER)

    else:
        speak("good Evening " + MASTER)

    speak("i am your assistant. How may I help you?")

def sendEmail(to, content): #here we define a funtion name called sendemail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_id_list ={"bhanu":"mail_id of bhanu","neeraj":"mail_id of bhanu","vinay":"mail_id of bhanu"}
    server.ehlo()
    server.starttls()
    server.login('User-email-id', 'Password')# login detail of the user 
    server.sendmail(to,content)
    server.close()



#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer() # here we declare variable r as recognizer
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)# here what user is said is saved in listen(source)

    try :      
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in') # here user query(audio) will be recognized with google in english
        print(f"user said: {query}\n") # here system will print what used said

    except Exception as e:
        speak("Say that again please...")
        return None
    #query=query.lower()
    #return query
    

#main program starting
def main():
    speak("Initializing OSIS...")
    wishMe()
    query = takeCommand()

    #Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open('youtube.com')
        url = "youtube.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        #webbrowser.open('google.com')
        url = "google.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open blackboard' in query.lower():
        #webbrowser.open('blackboard.com')
        url = "cuchd.blackboard.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

        # username_textbox = driver.find_element_by_id("user_id")
        # username_textbox.send_keys("")

        # password_textbox = driver.find_element_by_id("password")
        # password_textbox.send_keys("")

        # Popup_textbox = driver.find_element_by_class_name("button-1")
        # Popup_textbox.click()

        # login_button = driver.find_element_by_xpath("//input[@name='login'][@type='submit']")
        # login_button.click()
        

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Legion\\Desktop\\audio"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")
        print(strTime)

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\LEGION\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'open Steam' in query.lower():
        codePath = "C:\\Program Files (x86)\\Steam\\steam.exe"
        os.startfile(codePath)
            
    elif 'send message' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = "sainibhanu96@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent to bhanu")
        except Exception as e:
            print(e)

main()