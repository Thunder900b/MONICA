import sys
import time

import pyautogui

import wikipedia
import speech_recognition
import webbrowser
import os
import pyttsx3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# speech function:
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[5].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good morning sir.")

    elif 12 <= hour <= 18:
        speak("Good afternoon sir.")

    else:
        speak("Good evening sir!")


def Weather():
    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q=Berhampore&appid=acbefdb636599782c0d22f30f4f954d5"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        print("Invalid city address")

    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        date = datetime.now().strftime("%d %b %Y")
        times = datetime.now().strftime("%I %M %p")

        speak("Current temperature is: {:.2f}°C".format(temp_city))
        speak("wind is blowing in {} kilometre per Hour, with {} % humidity,and with {}".format(wind_speed, humidity,
                                                                                                weather_desc))
        speak("It's {}".format(date))
        speak("and the time is {}".format(times))

        print("Current temperature is: {:.2f}°C".format(temp_city))
        print("wind is blowing in {} kilometre per Hour, with {} % humidity,and with {}".format(wind_speed, humidity,
                                                                                                weather_desc))
        print("It's {}".format(date))
        print("and the time is {}".format(times))


def temperature():
    search = "temperature my locality"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current temperature is {temp}")


def connection():
    url = "https://google.com"
    timeout = 5

    try:
        request = requests.get(url, timeout=timeout)
        speak("connected to internet.")
    except:
        speak("Not connected to internet. I cannot work without internet connectivity.")


def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        quary = r.recognize_google(audio, language='bengali')
        print("User said:", quary)

    except Exception as e:
        print(e)
        print("Sorry! Abaer bolun please?...")
        return "None"
    return quary


def Task_Execution():
    speak("MONICA ON YOUR service")
    while True:
        quary = takecommand().lower()

        if 'tell me about' in quary:
            speak("dekhhchi daaaraaan!")
            quary = quary.replace("tell me about", "")
            results = wikipedia.summary(quary, sentences=4)
            speak("wikipedia anujai")
            print(results)
            speak(results)

        elif 'youtube' in quary:
            chromepath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chromepath))

            webbrowser.open("youtube.com")


        elif 'Facebook' in quary:
            webbrowser.open("facebook.com")


        elif 'google' in quary:
            speak("sir, what should I search on google?")
            chromepath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chromepath))

            com = takecommand().lower()
            webbrowser.open(f"{com}")

        elif 'music' in quary:
            music_dir = 'D:\\arif\\music_dir'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        # Date and time:

        elif 'sleep' in quary:
            speak("ok! as you wish!")
            break

        elif 'stop' in quary:
            speak("ok! as you wish!")
            break

        elif 'hello' in quary:
            speak("o hello sir!")

        elif 'good night' in quary:
            speak("goodnight! Call me if you want me again.")
            break

        elif 'stop' in quary:
            speak("ok! as you wish!")
            break

        #        elif 'temperature' in quary:
        #            search = "temperature my locality"
        #            url = f"https://www.google.com/search?q={search}"
        #            r = requests.get(url)
        #           data = BeautifulSoup(r.text, "html.parser")
        #           temp = data.find("div", class_="BNeawe").text
        #            speak(f"current{search} is {temp}")

        elif 'weather' in quary:
            complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q=Berhampore&appid=acbefdb636599782c0d22f30f4f954d5"
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            if api_data['cod'] == '404':
                print("Invalid city address")

            else:
                temp_city = ((api_data['main']['temp']) - 273.15)
                weather_desc = api_data['weather'][0]['description']
                humidity = api_data['main']['humidity']
                wind_speed = api_data['wind']['speed']
                date = datetime.now().strftime("%d %b %Y")
                times = datetime.now().strftime("%I %M %p")

                speak("Current temperature is: {:.2f}°C".format(temp_city))
                speak("wind is blowing in {} kilometre per Hour, with {} % humidity,and with {}".format(wind_speed,
                                                                                                        humidity,
                                                                                                        weather_desc))
                speak("It's {}".format(date))
                speak("and the time is {}".format(times))

                print("Current temperature is: {:.2f}°C".format(temp_city))
                print("wind is blowing in {} kilometre per Hour, with {} % humidity,and with {}".format(wind_speed,
                                                                                                        humidity,
                                                                                                        weather_desc))
                print("It's {}".format(date))
                print("and the time is {}".format(times))

        # Basic funda

        elif 'routine' in quary:
            webbrowser.open("file:///C:/Users/Dell/Downloads/Telegram%20Desktop/Routine_CST_CSIT_4th%20Semester.pdf")

        # Security
        elif 'security' in quary:
            zoom = "https://us05web.zoom.us/j/84695085778?pwd=NmtIbGM2TnRNNk8yUXNvSEtwVTdMZz09"
            webbrowser.open(zoom)

        # opening software tools:
        elif 'note' in quary:
            speak("opening note pad")
            apath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(apath)

        elif 'PyCharm' in quary:
            speak("opening note pad")
            bpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64"
            os.startfile(bpath)

        elif 'command prompt' in quary:
            speak("opening command prompt")
            os.system("start cmd")

        elif 'camera' in quary:
            speak("opening camera")

        # basic function

        elif 'shot' in quary:
            speak()

        elif 'switch' in quary:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'shutdown' in quary:
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            time.sleep(1)
            pyautogui.keyUp("alt")
            pyautogui.press("enter")




if __name__ == '__main__':

    speak("preparing to start programme. Checking internet connectivity.")
    connection()
    Weather()
    while True:
        permition = takecommand()
        if 'wake up' in permition:
            Task_Execution()
        elif 'goodbye' in permition:
            speak("Ok sir! Thanks for using me.")
            sys.exit()
