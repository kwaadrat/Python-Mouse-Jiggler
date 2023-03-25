
import pyautogui
from time import sleep
import os

x_string = input('Insert time in minutes: ')

pyautogui.hotkey('command', 'tab')

i = int(x_string)

i = i * 60

x = 15
y = 15

for i in range(i):
    pyautogui.moveTo(x, y)
    pyautogui.moveTo(x, y)
    print(i)
    sleep(1)
    x = x + 1
    y = y + 1