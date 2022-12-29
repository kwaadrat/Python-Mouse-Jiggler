
import pyautogui
from time import sleep
import os

x_string = input('Insert time in minutes: ')

pyautogui.hotkey('alt', 'tab')

x = int(x_string)

x = x * 60

for x in range(x):
    pyautogui.moveTo(1900, 1060)
    pyautogui.moveTo(1901, 1061)
    print(x)
    sleep(1)