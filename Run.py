#!python3

import time
import os
import cv2
import pyautogui as pag
import numpy as np

def getUser():
    return email, password

def readImage(path : str):
    return cv2.imread(path)

def doTheThing(email, password):
    pag.typewrite(email)
    time.sleep(0.1)
    pag.press('tab')
    pag.typewrite(password)
    time.sleep(0.1)
    pag.press('enter')

def findImage(screen, image, threshold):
    res = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return loc

def isEmpty(array):
    return not list(array[0])

def compress(screen, sample, rate):
    return resize(screen, rate), resize(sample, rate)

def locateOnScreen(image):
    screen = getScreen()
    compression = 0.5
    screen, image = compress(screen, image, compression)
    threshold = 0.70
    loc = findImage(screen, image, threshold)  
    return not isEmpty(loc)

def pilToNumpy(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def resize(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

def getScreen():
    screen = pag.screenshot()
    screen = pilToNumpy(screen)
    return screen

def showImageTest(image):
    cv2.imshow('image',image)
    cv2.waitKey(0)

email = "my mail"
password = "my password"
sample_img = "login.png"
launcher = "C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe"

if __name__ == '__main__':
    print("Running Script...")
    email, password = getUser()
    os.startfile(launcher)
    sample = readImage(sample_img)
    time.sleep(2)
    while not locateOnScreen(sample):
        print("trying to locate element..")
        time.sleep(0.12)
    doTheThing(email, password)
