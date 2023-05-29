import pyzenbo
from pynput import keyboard

from pyzenbo.modules.dialog_system import RobotFace

host = open('ip.txt', "r", encoding="utf-8").read()
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
        elif key == keyboard.KeyCode.from_char('d'):
            chat_str = input("Your message: ")
            sdk.robot.speak(chat_str)
        elif key == keyboard.Key.f1:
            sdk.robot.speak("你好，我是禪寶，很高興認識你")
        elif key == keyboard.Key.f2:
            sdk.robot.speak("後退中，請注意")


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

