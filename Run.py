#!python3

import time
import os

import pyautogui as pag
if __name__ == '__main__':
    print("Running Script...")
    os.startfile("C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe")
    while not pag.locateOnScreen("login.png"):
        print("login.png not found on screen yet..")
        time.sleep(0.1) #wait until the game loads up
    pag.typewrite("Email") #Email here
    pag.press('tab')
    time.sleep(0.1)
    pag.typewrite("Password") #Password here
    pag.press('enter')