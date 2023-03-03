import pyautogui
import random

Scr = pyautogui.size()

wight = random.randint ( 0 , Scr.wight )

height = random.randint ( 0 , Scr.height )

while True:
    pyautogui.leftclick ( x = wight , y = height )