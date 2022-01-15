import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',140)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ")   

    else:
        speak("Good Evening")  

    speak("I am venom from india ! aateesh sir! tell me how may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
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

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open wether' in query:
            webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN978IN978&oq=weather&aqs=chrome..69i57j0i271l2.14153j0j15&sourceid=chrome&ie=UTF-8")
            

        elif 'play music' in query:
            music_dir = 'C:\\Users\Avita\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\Avita\OneDrive\Desktop\code note"
            os.startfile(codePath)

        elif 'email to ateesh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "AteeshyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")  
        elif 'girlfriend' in query:
            speak("Girl friend is a time pass ")
        elif 'life partner' in query:
            speak("for life partner meet sachin sir in pg room number 106 bed number4")
        elif 'chandigarh university' in query:
            speak("Chandigarh university is good but management is bakwass")        
        elif 'god' in query:
            speak("if god means creator i am also created so there is god")
        elif 'hello' in query:
            speak("hii ! how are you")
            
            
