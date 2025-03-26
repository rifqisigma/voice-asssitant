import speech_recognition as sr
import pyttsx3

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n Silakan bicara...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"Anda: {text}")
        return text
    except sr.UnknownValueError:
        print("Tidak bisa mengenali suara.")
        return None

def text_to_speech(text, gender):
    print(f"AI: {text}")
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")

    if gender == "male":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()
