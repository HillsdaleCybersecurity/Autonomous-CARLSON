import speech_recognition as sr
import pyttsx3
import datetime

# initialize text-to-speech engine
engine = pyttsx3.init()

# set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        speak('Sorry, I didn\'t catch that. Can you please repeat?')
        return "None"
    return query

# function to greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning,")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon,")
    else:
        speak("Good evening,")

    speak("my name is CARLSON, how may I be of service?")

# main program loop
if __name__ == "__main__":
    greet()
    while True:
        query = recognize_speech().lower()

        # logic for executing tasks based on query
        if 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'exit' in query:
            speak("Goodbye!")
            exit()
