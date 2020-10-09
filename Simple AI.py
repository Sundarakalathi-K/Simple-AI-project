import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil  #pip install psutil
import pyjokes #pip install pyjokes

engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    

def date():
    year =int(datetime.datetime.now().year)
    month =int(datetime.datetime.now().month)
    date =int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)    
    speak(month)
    speak(year)


def wishme():
    speak("Welcome Back sir!")
   
    time()
    
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour <16:
        speak("Good afternoon!")
    elif hour >=14 and hour <20:
        speak("good Evening!")
    else:
        speak("Good night!")           
    speak("Jarvis here!. Please tell me how can i help you sir!!")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")  
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please..")

        return "None"

    return query 


def  sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com') 
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','12345')
    server.sendmail('', to, content)
    server.close()    

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\sit19\\OneDrive\\Desktop\\ss.png")

def cpu():
    usage =  str(psutil.cpu_percent())
    speak('CPU is at '+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())




if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'time'in query:
            time()

        elif 'date' in query:
            date() 

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result) 

        elif 'sendmail'in query:
            try:
                speak('What should I say?')
                content = takecommand()
                to = 'xyz@gmail.com'
                # sendEmail(to,content)

                sendEmail(to,content)
                speak("Email has been sent sucessfully!!")
            except Exception as e:
                print(e)
                speak("Unable to send Email") 

        elif 'search in chrome' in query:
            speak("What should i search?")
            chromePath =  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'           
            search =takecommand().lower()
            wb.get(chromePath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -l")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            
        elif 'restart' in query:
            os.system("shutdown /r /t 1")    
        
        elif 'play songs' in query:
            songs_dir = 'E:\\songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'remember that' in query:
            speak("what should i remember?")
            data = takecommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+remember.read())


        elif 'screenshot' in query:
            screenshot()
            speak("screen shot has been captured")  


        elif 'cpu'in query:
            cpu()    


        elif 'joke' in query:
            jokes()          

        elif 'offline' in query:
            quit()    



