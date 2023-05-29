import pyzenbo, time
from pyzenbo.modules.dialog_system import RobotFace

result=dict()
def on_result(**kwargs):
    global result
    result = kwargs

host = open('ip.txt', "r", encoding="utf-8").read()
sdk = pyzenbo.connect(host)
sdk.on_result_callback = on_result
sdk.robot.set_expression(RobotFace.PLEASED, "開始前進")
sdk.motion.remote_control_body(1, True, 100)
for i in range(5):
    data = sdk.sensor.get_sonar(2,True, 10)
    try:
        dist = result['result']['SENSOR_VALUE']
        print(dist)
        sdk.robot.speak(str(round(dist*100))+"公分")
    except:
        pass
    time.sleep(2)
    
sdk.motion.remote_control_body(0, True,100)
sdk.robot.set_expression(RobotFace.PLEASED, "任務結束")
sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()