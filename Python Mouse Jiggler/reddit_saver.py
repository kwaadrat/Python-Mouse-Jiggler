from time import sleep
import pyautogui
import os

x = input("Wprowad ilość kart do zapisania: ")
x = int()
i = 0

while i == x:
    pyautogui.moveTo(900, 1060, 2, pyautogui.easeInOutQuad)
    sleep(1)
    pyautogui.moveTo(400, 450, 2, pyautogui.easeInOutQuad)
    sleep(1)
    pyautogui.leftClick
    sleep(1)
    pyautogui.hotkey('command', 's')
    sleep(1)
    pyautogui.press('enter')
    #pyautogui.
    i = i + 1
    print(i)
else:
    print("Zapisano wszystkie obrazy")