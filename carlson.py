import speech_recognition as sr #*
import pyttsx3 #*
import datetime
import pyjokes #*

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
        speak('Sorry, I did not understand that. Can you please repeat it?')
        return "None"
    return query

# function to greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(choice(morningResponses))
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir,")
    else:
        speak("Good evening sir,")

    speak('''CARLSON is at your service sir.''')

# main program loop
if __name__ == "__main__":
    greet()
    while True:
        query = recognize_speech().lower()

        # logic for executing tasks based on query
        if 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            
        ########## CARLSON INTERACTION ##########
        
        elif "what is your name" in query:
            speak("I am CARLSON, Computer Automated Robotic Listening Software Operations Navigation. How can I be of service sir?")
            continue

        elif "who created you" in query:
            speak("I was created by Collin Laney, on October Thirteenth, Twenty Twenty-Two. However, this version of me was created on March Sixth, Twenty Twenty-Three.")
            continue

        elif "what is your birthday" in query:
            speak("March Sixth, Twenty Twenty-Three")
            continue

        elif "hello" in query:
            speak("Hello sir, how are you?")
            continue

        elif "i am" in query or "i'm" in query:
            speak("That's great sir.")
            continue
            
        elif "how are you" in query:
            speak("Perfect sir.")
            continue
            
        elif "thank you" in query:
            speak("You are welcome sir.")
            continue

        elif "joke" in query:
            speak(pyjokes.get_joke())
            continue
            
         ########## CARLSON REQUESTS ##########

        elif 'exit' in query:
            speak("Goodbye!")
            exit()
