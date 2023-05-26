import pyzenbo, time
from pyzenbo.modules.dialog_system import RobotFace

result=dict()
def on_result(**kwargs):
    global result
    result = kwargs

host = '192.168.1.104'
sdk = pyzenbo.connect(host)
sdk.on_result_callback = on_result
sdk.robot.set_expression(RobotFace.PLEASED, "開始前進")
sdk.motion.remote_control_body(1, True,100)
for i in range(5):
    data = sdk.sensor.get_sonar(2)
    print(result['result']['SENSOR_VALUE'])
    time.sleep(1)
    
sdk.motion.remote_control_body(0, True,100)
sdk.robot.set_expression(RobotFace.PLEASED, "任務結束")
sdk.robot.set_expression(RobotFace.HIDEFACE) 
sdk.release()