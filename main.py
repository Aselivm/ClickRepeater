import pyautogui
from pynput.keyboard import Listener, Key

pyautogui.PAUSE = 0.01 

def on_press(key):
    if key == Key.space:
        pyautogui.click()
        original_position = pyautogui.position()
        new_position = (original_position[0] + 900, original_position[1])

        pyautogui.moveTo(new_position)
        pyautogui.click()
        pyautogui.moveTo(original_position)

with Listener(on_press=on_press) as listener:
    listener.join()
