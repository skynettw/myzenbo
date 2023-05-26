import pyzenbo
import openai
from pyzenbo.modules.dialog_system import RobotFace

host = '192.168.1.104'
sdk = pyzenbo.connect(host)
key = open("key.txt", "r", encoding="utf-8").read()
openai.api_key= key
response = openai.Completion.create(
    engine = "gpt-3.5-turbo",    # select model
    prompt = "ChatGPT是什麼？",     
    max_tokens = 512,               # response tokens
    temperature = 1,                # diversity related
    top_p = 0.75,                   # diversity related
    n = 1,                          # num of response
)

completed_text = response["choices"][0]["text"]
print(completed_text)

sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()