
import pyautogui
from time import sleep
import os

x = input('Insert time in minutes: ')

x = x * 60

for x in range(x):
    pyautogui.moveTo(1900, 1060)
    pyautogui.moveTo(1901, 1061)
    print(x)
    sleep(1)
    clear = lambda: os.system('cls')
    clear()