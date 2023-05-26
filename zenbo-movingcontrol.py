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
            sdk.motion.move_body(0.1, 0, 0, 1, True, 10)
        elif key == keyboard.Key.down:
            sdk.motion.move_body(-0.1, 0, 0, 1, True, 10)
        elif key == keyboard.Key.left:
            sdk.motion.move_body(0, 0, 10, 1, True, 10)
        elif key == keyboard.Key.right:
            sdk.motion.move_body(0, 0, -10, 1, True, 10)
    

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

