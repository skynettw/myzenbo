import pyzenbo
import time
from pyzenbo.modules.dialog_system import RobotFace

host = open('ip.txt', "r", encoding="utf-8").read()
sdk = pyzenbo.connect(host)
name = sdk.robot.speak_and_listen('請問你叫什麼名字', timeout=5)
print(name)
sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()