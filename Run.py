#!python3

import time
import os
import cv2
import pyautogui as pag

def getUser():
    return "email", "pass"

if __name__ == '__main__':
    print("Running Script...")
    sample_img = "login.png"
    email, password = getUser()
    
    os.startfile("C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe")
    
    while not pag.locateOnScreen():
        print("login.png not found on screen yet..")
        time.sleep(0.1) #wait until the game loads up
    
    pag.typewrite(email) #Email here
    pag.press('tab')
    time.sleep(0.1)
    pag.typewrite(password) #Password here
    pag.press('enter')