
import pyautogui
from time import sleep
import os

x_string = input('Insert time in minutes: ')

pyautogui.hotkey('command', 'tab')

x = int(x_string)

x = x * 60

for x in range(x):
    pyautogui.moveTo(190, 10)
    pyautogui.moveTo(19, 10)
    print(x)
    sleep(1)