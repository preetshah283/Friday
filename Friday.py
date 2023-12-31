
'''
# beginner
1. Respond to "hello".
2. Provide predefined responses(mrng,evng,aftnn).
3. Time, date.
4. Searching the web for user queries.
'''
'''
#advanced
1. Advanced voice assistant with natural language processing capabilities. 
2. Sending emails
3. Setting reminders
4. Providing weather updates
5. Controlling smart home devices
6. Answering general knowledge questions
7. Integrating with third-party APIs for more functionality.
'''

import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia as wiki
import smtplib

#---------------------------------------------------------------------------ENGINE INIT
engine = pyttsx3.init() #init the speech recognition engine
engine.setProperty("rate",180) #set the speech rate to 180 wpm

voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice",voices[1].id)

#---------------------------------------------------------------------------SAYING THE TEXT(USER SPOKEN OR ENTERED)
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

#---------------------------------------------------------------------------TAKING WRITTEN INPUT
def take_written_input(message):        #! Takes written input from user 
    talk(message)
    return input("Type your answer here ----> ").lower()

#---------------------------------------------------------------------------GREETING BASED ON TIME
def greetings(greet):
    if greet >= 5 and greet < 12:
        talk("Good morning!, what can I do for you?")
    elif greet>=12 and greet<17:
        talk("Good Afternoon!, what can I do for you?")
    elif greet>=17 and greet<24:
        talk("Good Evening!, what can I do for you?")
    elif greet>=0 and greet<5:
        talk("You should go to sleep.. But, what can I do for you?")

#---------------------------------------------------------------------------SPEECH RECOGNISATION
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
        print("I think you said:- " + text)

    except sr.UnknownValueError:
        print("Sorry, I can't understand what you just said. Could you speak that again?")
        text = ""

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        text = ""

    return text

#--------------------------------------------------------------------------- SENDING EMAILS
def send_email(subject,receivers_email,body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'shahpreet2803@gmail.com' 
    sender_password = 'iefk jalo vkic gixg'  #app specific password used
    # subject = this.subject
    # receivers_email = "d36191973@gmail.com"  #dummy email address
    # body = "generated email"
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            msg = f'Subject: {subject}\n\n{body}'
            server.sendmail(sender_email, receivers_email, msg)
            print(f"Email sent to {receivers_email}")
    except Exception as e:
        print(f"Error sending email to {receivers_email}: {str(e)}")

#---------------------------------------------------------------------------VARIABLES FOR ANSWERING
time = datetime.now().time()
date = datetime.now().date().strftime("%d/%m/%Y") #to change the date format

#---------------------------------------------------------------------------RESPONSES ACCORDING TO QUERIES
greetings(time.hour)
query = listen().lower()

if "time" in query: #tell me the time
    text = time
    talk(text)

if "date" in query: #tell me the date
    text = date
    talk(text)

if "wikipedia" in query or "about" in query or "search" in query or "tell" in query:  # tell me about Python from wikipedia
        query = query.replace("wikipedia", "")
        if "from" in query:
            query = query.replace("from", "")
        if "tell me":
            query = query.replace("tell me", "")
        if "something":
            query = query.replace("something", "")
        if "about":
            query = query.replace("about", "")
        if "search":
            query = query.replace("search","")
        # print("Query =", query)
        response = wiki.summary(query, sentences=2)
        talk(response)

if "email" in query:
    talk("Speak in the following format: ")
    talk("Speak subject: ")
    subject = listen()
    talk("Written input activated.. ")
    receivers_email = take_written_input("Type email of receiver: ")
    talk("Speak email body: ")
    body = listen()
    send_email(subject,receivers_email,body)
