import speech_recognition as sr
import pyzenbo
import openai
from pyzenbo.modules.dialog_system import RobotFace

host = open('ip.txt', "r", encoding="utf-8").read()
sdk = pyzenbo.connect(host)
key = open("key.txt", "r", encoding="utf-8").read()
openai.api_key= key
r = sr.Recognizer()

def get_prompt():
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = r.listen(source=source, timeout=5)
        text = r.recognize_google(audio_data, language='zh-TW')
        print(text)
        return text
    
prompt = get_prompt()
while "結束" not in prompt:
    if prompt !="":
        sdk.robot.set_expression(RobotFace.PLEASED, "你剛剛問我，"+prompt)
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.7,
            max_tokens=100,
            n=1,
            stop=None,
        )
        reply = response.choices[0].text.strip()
        sdk.robot.speak("我的回答是："+reply)
        sdk.robot.speak("你還有什麼想問的嗎？")
    prompt = get_prompt()
sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()