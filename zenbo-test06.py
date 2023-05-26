import pyzenbo
import openai
from pyzenbo.modules.dialog_system import RobotFace

host = '192.168.1.104'
sdk = pyzenbo.connect(host)
key = open("key.txt", "r", encoding="utf-8").read()
openai.api_key= key

sdk.robot.speak("你有什麼想問的嗎？")
prompt = input("Your prompt: ")
while prompt != "exit" and prompt !="":
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
    prompt = input("Your prompt: ")
sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()