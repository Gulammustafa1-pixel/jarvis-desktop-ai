import pyttsx3


def speak(text):
    if not text:
        return

    engine = pyttsx3.init("sapi5")

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.say(str(text))
    engine.runAndWait()

    del engine