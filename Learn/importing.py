from math import * # importing everything from a built-in module
from random import randint # importing specific function
print("Floor of 8.9999 is", floor(8.9999))
print("Ceil of 9.0001 is", ceil(9.0001))
print("Random Number [1-100]:",randint(1, 100))

from test import Pout # importing function from other file
from test import take_list as listing # renaming the function for here
Pout("An outsider Function")
listing(1,3,5,7,9)

# Install PyAutoGUI from cmd "pip install pyautogui"
import pyautogui
for i in range(3):
    pyautogui.write('Py Spammer XD', interval=0.25)
    pyautogui.press('enter')
#! pyautogui will start typing automatically on your screen
#! Put cursor below this line before running this code