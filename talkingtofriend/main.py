import speech_recognition as sr
import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print("🤖 Bot:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
            command = recognizer.recognize_google(audio)
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            talk("Sorry, I didn't understand that.")
            return ""
        except sr.WaitTimeoutError:
            talk("I didn’t hear anything. Please try again.")
            return ""
        except sr.RequestError:
            talk("Sorry, I couldn't reach the speech service.")
            return ""

# 🌙 Emotional support responses with Quranic ayahs
responses = {
    "hello": "Salam Noor! I’m happy to hear your voice!",
    "i am feeling down": "‘Indeed, with hardship comes ease.’ – Surah Ash-Sharh (94:6)",
    "i feel alone": "‘Do not grieve; indeed Allah is with us.’ – Surah At-Tawbah (9:40)",
    "i am sad": "‘Verily, in the remembrance of Allah do hearts find rest.’ – Surah Ar-Ra’d (13:28)",
    "i am worried": "‘And whoever relies upon Allah – then He is sufficient for him.’ – Surah At-Talaq (65:3)",
    "i feel hopeless": "‘So truly where there is hardship, there is also ease.’ – Surah Ash-Sharh (94:6)",
    "i feel broken": "‘Despair not of the mercy of Allah.’ – Surah Az-Zumar (39:53)",
    "i feel like giving up": "‘And be not weak, and do not grieve, and you will be superior if you are true believers.’ – Surah Aal-E-Imran (3:139)",
    "i need strength": "‘Allah does not burden a soul beyond that it can bear.’ – Surah Al-Baqarah (2:286)",
    "i feel scared": "‘Allah is sufficient for us, and He is the best disposer of affairs.’ – Surah Aal-E-Imran (3:173)",
    "i feel unloved": "‘My mercy encompasses all things.’ – Surah Al-A’raf (7:156)",
    "i want to give up": "‘Verily, with every difficulty there is relief.’ – Surah Ash-Sharh (94:6)",
    "i feel like no one understands": "‘Indeed, my Lord is near and responsive.’ – Surah Hud (11:61)",
    "i feel anxious": "‘Unquestionably, by the remembrance of Allah hearts are assured.’ – Surah Ar-Ra’d (13:28)"
}

# 🌟 Main loop
talk("As-salamu Alaikum Noor. I’m ready to talk with you.")

while True:
    command = listen()

    if not command:
        continue

    if "stop" in command or "bye" in command:
        talk("Okay Noor, I’ll talk to you later. Take care 💖")
        break

    found = False
    for key in responses:
        if key in command:
            talk(responses[key])
            found = True
            break

    if not found:
        talk("I’m still learning... Can you try saying something else?")


