import pyzenbo
from pynput import keyboard

from pyzenbo.modules.dialog_system import RobotFace

host = '192.168.1.104'
sdk = pyzenbo.connect(host)

def on_press(key):
    if key == keyboard.Key.esc:
        listener.stop()
        sdk.robot.set_expression(RobotFace.HIDEFACE) 
        sdk.release()

    else:
        if key == keyboard.Key.up:
            sdk.motion.remote_control_body(0)
            sdk.motion.remote_control_body(1)
        elif key == keyboard.Key.down:
            sdk.motion.remote_control_body(0)
            sdk.motion.remote_control_body(2)
        elif key == keyboard.Key.left:
            sdk.motion.remote_control_body(0)
            sdk.motion.remote_control_body(3)
        elif key == keyboard.Key.right:
            sdk.motion.remote_control_body(0)
            sdk.motion.remote_control_body(4)
        elif key == keyboard.Key.space:
            sdk.motion.remote_control_body(0)

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

