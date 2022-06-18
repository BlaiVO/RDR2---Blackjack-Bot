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

def get_value():
    img = pyautogui.screenshot(region=(435,1003,135,25))
    value = tess.image_to_string(img)
    value = re.sub("[^0-9]", "", value)
    if value != "":
        value = int(value)
    else:
        print("Got no value, defaulting to 11")
        value = 11
    return value

def get_state():
    bet_img = pyautogui.screenshot(region=(1650,930,200,50))
    hit_img = pyautogui.screenshot(region=(1725,925,110,50))
    ins_img = pyautogui.screenshot(region=(1635,925,200,50))
    if "place bet" in tess.image_to_string(bet_img).lower():
        state = "bet_state"
    elif "stand" in tess.image_to_string(hit_img).lower():
        state = "play_state"
    elif "insurance bet" in tess.image_to_string(ins_img).lower():
        state = "insurance_state"
    else:
        state = "waiting"
    return state

    

time.sleep(2)

while True:

    state = get_state()

    if state == "bet_state":
        print("\nNow I bet")
        HoldAndReleaseKey(ENTER, 0.2)
        currentHits = 0
    
    elif state == "play_state":
        time.sleep(0.6)
        value = get_value()
        if value >= 17:
            print(f"Now I stand ({value})")
            HoldAndReleaseKey(S, 0.2)
        else:
            print(f"Now I hit ({value})")
            HoldAndReleaseKey(H, 0.2)
    
    elif state == "insurance_state":
        print("Now I insure")
        key = random.choice([ENTER, F])
        HoldAndReleaseKey(key, 0.2)

# insurance bet: region=(1635,925,200,50)    
# place bet: region=(1650,930,200,50)
# hit: region=(1725,975,110,50)
# stand: region=(1725,925,110,50)
# value: region=(435,1003,135,25)