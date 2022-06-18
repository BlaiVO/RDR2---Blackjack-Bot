from pyautogui import *
import pyautogui
import random
import ctypes
import pynput
import time
import re
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Users\blaix\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

#THE CODE TO SEND INPUT TO THE GAME IS MADE BY THE YOUTUBER DOUGDOUG #
SendInput = ctypes.windll.user32.SendInput
def HoldKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def HoldAndReleaseKey(hexKeyCode, seconds):
    HoldKey(hexKeyCode)
    time.sleep(seconds)
    ReleaseKey(hexKeyCode)

H = 0x23
S = 0x1F
F = 0x21
ENTER = 0x1C

#FROM THIS POINT ALL THE CODE IS MINE#

def readValue():
    img = pyautogui.screenshot(region=(420,1005,50,20))
    got_value = False
    while not got_value:
        raw_value = tess.image_to_string(img)
        try:
            value = re.sub("[^0-9]", "", raw_value)
        except ValueError:
            got_value = "error"
        got_value = True if not got_value == "error" else False
    return value

def getValue():
    isValueInt = False
    while not isValueInt:
        try:
            value = int(readValue())
        except ValueError:
            isValueInt = "error"
        isValueInt = True if not isValueInt == "error" else False
    return value

time.sleep(2)

while True:
    if pyautogui.locateOnScreen("insurance.png", region=(1600,750,300,300), confidence=0.7) != None:
        print("Now I insure")
        key = random.choice([ENTER, F])
        HoldAndReleaseKey(key, 0.2)
    
    elif pyautogui.locateOnScreen("hit.png", region=(1600,750,300,300), confidence=0.6) != None:
        time.sleep(0.6)
        if getValue() >= 17:
            print("Now I stand")
            HoldAndReleaseKey(S, 0.2)
        else:
            print("Now I hit")
            HoldAndReleaseKey(H, 0.2)

    elif pyautogui.locateOnScreen("bet.png", region=(1600,875,300,100), confidence=0.7) != None:
        print("Now I bet")
        HoldAndReleaseKey(ENTER, 0.2)
        currentHits = 0

    
