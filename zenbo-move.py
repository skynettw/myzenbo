import pyzenbo
import time
from pyzenbo.modules.dialog_system import RobotFace

host = open('ip.txt', "r", encoding="utf-8").read()
sdk = pyzenbo.connect(host)
sdk.robot.speak("出發！")
for i in range(10):
    sdk.motion.move_body(0.1, 0, -36, 1, True, 10)
sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()
