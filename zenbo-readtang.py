import pyzenbo
import time
from pyzenbo.modules.dialog_system import RobotFace
tang = "床前明月光,疑是地上霜,舉頭望明月,低頭思故鄉".split(',')

host = open('ip.txt', "r", encoding="utf-8").read()
sdk = pyzenbo.connect(host)
for s in tang:
    sdk.robot.set_expression(RobotFace.PLEASED, s)
    time.sleep(1)

sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()