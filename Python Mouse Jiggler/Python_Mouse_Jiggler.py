
import pyautogui
from time import sleep
import os

#x_string = input('Insert time in minutes: ')

pyautogui.hotkey('command', 'tab')

#i = int(x_string)
i = 1

#i = i * 60

x = 640
y = 480

print("\033c\033[3J")

for i in range(5000):
    pyautogui.moveTo(x, y)
    pyautogui.moveTo(x, y)
    print(x, "x", y)
    #sleep(1)
    #x = x + 1
    #y = x + 2

    while x > 1500 or y > 1050:
        y = 20
        x = 20
    else:
        x = x + 1
        y = y + 3
