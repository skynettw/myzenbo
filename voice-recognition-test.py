import speech_recognition as sr

r = sr.Recognizer()
text = ""
while "結束" not in text:
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio_data = r.listen(source=source, timeout=5)
            text = r.recognize_google(audio_data, language='zh-TW')
            print(text)
        except:
            text = ""
print("Bye!")