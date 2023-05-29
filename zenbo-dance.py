import pyzenbo, time
from pyzenbo.modules.dialog_system import RobotFace

host = open('ip.txt', "r", encoding="utf-8").read()
sdk = pyzenbo.connect(host)

sdk.robot.set_expression(RobotFace.PLEASED, "我要開始表演囉")
sdk.wheelLights.start_glowing_yoyo(0, 1, True, 100)
sdk.utility.play_action(15, True, 100)
sdk.wheelLights.turn_off(0)
sdk.robot.set_expression(RobotFace.PLEASED, "表演結束，謝謝收看")
sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()