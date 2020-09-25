from datetime import time
import pyttsx3, datetime, speech_recognition as sr, wikipedia, webbrowser as wb, os, random, json, requests, pyautogui as p, time
from time import time as t_func
from news_reporter import general_news, tech_news
p.FAILSAFE = True
from weather_monitor import weather
from Snakewatergun import snake_water_gun
from Guess_number import guess_number
from email_sender import send_mail

def male_voice(self, string):
    converter = pyttsx3.init() 
    converter.setProperty('rate', 190) 
    converter.setProperty('volume', 0.7) 
    converter.say(string) 
    converter.runAndWait() 


def female_voice(self, string):
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    converter = pyttsx3.init() 
    converter.setProperty('rate', 190) 
    converter.setProperty('volume', 0.8)
    converter.setProperty('voice', voice_id) 
    converter.say(string)
    converter.runAndWait() 

class Voices:
    def speak(self, audio):
        """speaks the given argument"""
        engine = pyttsx3.init('sapi5')
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[0].id)
        engine.say(audio)
        engine.runAndWait()
    
a = Voices()

def wish():
    """wishes the user according to time"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 20 and hour <= 24:
        a.speak("Night time working sir!")
    elif hour >= 2 and hour <=12:
        a.speak("Good moring sir!")
    elif hour>12 and hour<4:
        a.speak("Good afternoon sir!")
    else:
        a.speak("Good evening sir!")
    a.speak("How can I help you?")

def command():
    """taking user mic input as a command"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:  
        print("Say that again please...") 
        return "None"
    return query

def zoom_meeting(subject_id, password):
    """func which takes subject id and password as an argument and, basically zoom automation"""
    time.sleep(5)
    p.click(530, 281)
    time.sleep(2)
    p.click(651, 323)
    time.sleep(1)
    p.typewrite(subject_id)
    p.press('enter')
    time.sleep(5)
    p.typewrite(password)
    p.press('enter')
    
def screen_recording():
    """automate screen recording"""
    screen_recorder_target = r"C:\Program Files (x86)\Icecream Screen Recorder\recorder.exe"
    a.speak("Opening ice cream screen recorder")
    os.startfile(screen_recorder_target)
    time.sleep(10)
    p.click(416, 177, 2)
    p.click(407, 209)
    p.doubleClick(736, 709)
    p.typewrite("1366", 2)
    p.doubleClick(813, 719)
    p.typewrite('687', 2)
    a.speak("You're ready to record, just press F7 to continue. Say stop screen recording to stop it.")

def cwh_course(playlist_url):
    """opens firefox and then opens any cwh course"""
    os.startfile(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    time.sleep(5)
    p.typewrite(playlist_url)
    p.press('enter')

def access_web(url):
    os.startfile(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    time.sleep(3)
    p.typewrite(url)
    p.press('enter')

if __name__ == "__main__":
    wish()
    zoom_counter = 0
    screen_counter = 0
    timer_counter = 0
    stopwatch_counter = 0
    while 1:
        query = command().lower()

        if 'wikipedia' in query:
            try:
                a.speak("Searching through the wikipedia for your query...Hang on..")
                query = query.replace('wikipedia', "")
                result = wikipedia.summary(query, sentences = 2)
                a.speak("According to wikipedia...")
                print(result)
                a.speak(result)
            except ConnectionError as e:
                a.speak("Check your network")
            except Exception as e:
                a.speak(e)

        elif 'quit jarvis' in query or 'get lost' in query or 'f***' in query or 'shut' in query or 'stop listening' in query:
            a.speak("Thanks for visiting sir!")
            quit()

        elif 'who you' in query:
            a.speak("Hello sir, I am Jarvis, an intelligent AI made by Shravan with python.")

        elif 'how are you' in query:
            a.speak("I am alright! How about you?")
            response = command().lower()
            if 'fine' in response or 'alright' in response:
                a.speak("Glad to hear that!")


        elif 'open youtube' in query:
            wb.open('youtube.com')

        elif 'open google' in query:
            wb.open('google.com')

        elif 'open stack overflow' in query:
            wb.open('stackoverflow.com')

        elif 'google' in query.lower():
            query = query.replace("google", "")
            wb.open(f'google.com')
            time.sleep(5)
            p.typewrite(query)
            p.press('enter')


        elif 'open github' in query:
            access_web('https://github.com/Shravan-1908/First_Repo')

        elif 'open instagram' in query:
            access_web('https://www.instagram.com/')
        
        elif 'play music' in query or 'music' in query:
            music_path = r"C:\Users\Lenovo\Documents\Music and Projects'\EDM Music\Favorites"
            songs = os.listdir(music_path)
            a.speak("Playing songs from your favorites...")
            for i in songs:
                if i.endswith(".mp3"):
                    playable = random.choice(songs)
                    os.startfile(os.path.join(music_path, playable))
                    break

        elif 'you hear' in query:
            a.speak("I usually hear EDM. My favorite artist is Illenium.")
            a.speak("Do you want to know more about Illenium?")
            response = command().lower()
            if response == 'yes' or response == 'why not':
                a.speak("Grabbing some info about Illenium...Wait a few seconds..")
                result = wikipedia.summary("Illenium", sentences = 2)
                print(result)
                a.speak(result)

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H-%M")
            print(f"The current time is {strTime}")
            a.speak(f"The current time is {strTime}")


        elif 'general news' in query:
            a.speak("Hold up..")
            general_news(2)

        elif 'tech news' in query:
            a.speak("Hold up..")
            tech_news(2)

        elif 'weather' in query:
            try:
                query = query.replace('weather', "")
                a.speak(f"Fetching weather for {query.strip()}")
                weather(query.strip().capitalize())
            except Exception as e:
                a.speak("Some error occured!")
                a.speak(e)


        elif 'open code' in query or 'i code in python' in query:
            code_target = r"C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            a.speak("Opening Visual Studio Code...")
            os.startfile(code_target)

        elif 'open sublime' in query or 'quick code' in query:
            sublime_target = r"C:\Program Files\Sublime Text 3\sublime_text.exe"
            a.speak("Opening Sublime Text...")
            os.startfile(sublime_target)

        elif 'open java ide' in query or 'i code in java' in query:
            intellij_target = r"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2020.2\bin\idea64.exe"
            a.speak("Opening IntelliJ IDEA...")
            os.startfile(intellij_target)

        elif 'open scratch' in query:
            a.speak("Opening scratch...")
            scratch_target = r"C:\Program Files (x86)\Scratch 2\Scratch 2.exe"
            os.startfile(scratch_target)

        elif 'open spotify' in query:
            a.speak("Opening spotify...")
            p.press('winleft', 1)
            p.typewrite('Spotify')
            p.press('enter')

        elif 'open zoom' in query or 'class time' in query or 'meeting time' in query:
            zoom_target = r"C:\Users\Lenovo\AppData\Roaming\Zoom\bin\Zoom.exe"
            sub_pass = {"7207522193":"1357", "3480809136":"1010", "4529209557":"12030411"}
            a.speak("Any particular class you want me to fill info of?")
            response = command().lower()
            if 'no' in response:
                a.speak("Alright! Opening zoom...")
                os.startfile(zoom_target)
            elif 'maths' in response or 'biology' in response:
                a.speak("Alright.. I hope he teaches and doesnt send photos on whatsapp!")
                os.startfile(zoom_target)
                time.sleep(3)
                zoom_meeting("7207522193", "1357")
            elif 'hindi' in response:
                a.speak("Alright.. I hope he wont let you write much today!!")
                os.startfile(zoom_target)
                time.sleep(3)
                zoom_meeting("3480809136", "1010")
            elif 'social science' in response or 'chemistry' in response:
                a.speak("Alright.. Dont forget to pay attention..!")
                os.startfile(zoom_target)
                time.sleep(3)
                zoom_meeting("4529209557", "12030411")
            a.speak("If you want to have the meeting controls, just say meeting controls")
            zoom_counter += 1 

        elif 'meeting control' in query:
            if zoom_counter < 1:
                a.speak("You arent in any meeting right now!")
            else:
                a.speak("Ok what to do?")
                response = command().lower()
                if 'leave meeting' in response or 'quit meeting' in response:
                    p.hotkey('alt', 'f4')
                    
        elif 'start screen recording' in query:
            screen_recording()
            screen_counter += 1

        elif 'stop screen recording' in query:
            if screen_counter < 1:
                a.speak("No active screen recording right now!")
            else:
                p.hotkey('f8')

        elif 'open file explorer' in query:
            a.speak("Opening File Explorer....")
            p.hotkey('winleft', 'e')

        elif 'open chrome' in query:
            chrome_target = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            a.speak("Opening Google Chrome....")
            os.startfile(chrome_target)

        elif 'open firefox' in query:
            firefox_target = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
            a.speak("Opening Mozilla Firefox...")
            os.startfile(firefox_target)

        elif 'open calculator' in query:
            a.speak("Opening calculator...")
            p.press('winleft')
            p.typewrite("Calculator")
            p.press('enter')

        elif 'open whatsapp' in query:
            a.speak("Opening whatsapp....")
            p.press('winleft')
            time.sleep(2)
            p.typewrite('Whatsapp')
            p.press('enter')

        elif 'switch to last app' in query:
            a.speak("Switching...")
            p.hotkey('alt', 'tab')
        elif 'close the last app' in query:
            a.speak("Closing the last app opened...")
            p.hotkey('alt', 'tab')
            time.sleep(2)
            p.hotkey('alt', 'f4')


        elif 'snake water gun game' in query:
            a.speak("Launching Snake Water Gun game on the console.......Dont cheat ")
            snake_water_gun()
            
        elif 'guess the number game' in query:
            a.speak("Launching guess the number game on the console......Dont cheat ")
            guess_number()


        elif 'repeat after me' in query:
            a.speak("Ok I am listening....")
            response = command().lower()
            a.speak(response)


        elif 'learn python' in query:
            a.speak("Opening Code With Harry's python playlist...")
            cwh_course("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

        elif 'learn java' in query:
            a.speak("Opening Code With Harry's java playlist...")
            cwh_course("https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q")
            
        elif 'learn graphical user interface' in query:
            a.speak("Opening Code With Harry's Python GUI with Tkinter playlist...")
            cwh_course("https://www.youtube.com/playlist?list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA")

        elif 'send email' in query:
            a.speak("Alright to whom? Type the email address")
            to = input("Email address: ")
            a.speak("What's the subject of the mail?")
            subject = command()
            a.speak("a.speak the body of the mail?")
            body = command()
            send_mail(to, subject, body)

        elif 'check emails' in query:
            a.speak("Taking you to the yahoo mail")
            access_web("https://mail.yahoo.com/d/folders/1?.intl=in&.lang=en-IN&.partner=none&.src=fp&reason=timezone-mismatch&counter=1")

        elif 'joke' in query:
            a.speak("Fetching one...")
            r = requests.get("https://sv443.net/jokeapi/v2/joke/Programming,Miscellaneous,Pun?blacklistFlags=nsfw,religious,political,racist,sexist").text
            parse = json.loads(r)
            if parse['type'] == 'single':
                a.speak(f"{parse['joke']}")
            else:
                a.speak(f"{parse['setup']}")
                a.speak(f"{parse['delivery']}")


        elif 'start a timer' in query or 'set a timer' in query:
            if timer_counter % 2 == 0:
                a.speak("Alright..for how many minutes? ")
                minutes = int(input("Alright..for how many minutes? "))
                init = t_func()
                a.speak(f"Timer initiated for {minutes} minutes!")
                timer_counter += 1
            else:
                a.speak(f"One timer is already going on...")

        if timer_counter % 2 != 0:
            if (t_func() - init) > (minutes * 60):
                a.speak("Time up!")
                print("Time up!")
                os.startfile(r"C:\Users\Lenovo\Documents\Python Codes\piano result.mp3")
                timer_counter += 1

        elif 'start stopwatch' in query:
            if stopwatch_counter % 2 == 0:
                a.speak("Alright...Stopwatch initiated")
                stop_init = t_func()
                stopwatch_counter += 1
                a.speak("Stop the stopwatch to stop it")
            else:
                a.speak("One stopwatch already in progress")

        elif 'stop the stopwatch' in query:
            if stopwatch_counter % 2 == 0:
                a.speak("No stopwatch currently in progress..")
            else:
                interval = t_func() - stop_init
                stopwatch_counter += 1
                a.speak("Alright stopwatch stopped")
                print(f"It lasted for {interval} seconds")
                a.speak(f"It lasted for {interval} seconds")

        elif 'change your voice' in query:
            if Voices.speak != female_voice:
                a.speak("Ok changing voice")
                Voices.speak = female_voice
            else:
                a.speak("Ok changing voice")
                Voices.speak = male_voice
            a.speak("Hi sir! How can I help you?")