import pyautogui
from pynput.mouse import Listener, Button

pyautogui.PAUSE = 0.01

running = False

def on_click(x, y, button, pressed):
    global running

    if button == Button.left and not running:
        running = True
        pyautogui.click()

        original_position = pyautogui.position()
        new_position = (original_position[0] + 900, original_position[1])

        pyautogui.moveTo(new_position)
        pyautogui.click() 
        pyautogui.moveTo(original_position)

        running = False

with Listener(on_click=on_click) as listener:
    listener.join()