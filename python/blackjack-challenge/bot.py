from pyautogui import *
import pyautogui

import ctypes
import pynput

import time

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
ENTER = 0x1C

currentHits = 0

while True:
    if pyautogui.locateOnScreen("insurance.png", region=(1600,750,300,300), confidence=0.7) != None:
        print("Now I insure")
        HoldAndReleaseKey(ENTER, 0.2)

    elif pyautogui.locateOnScreen("hit.png", region=(1600,750,300,300), confidence=0.7) != None:
        if currentHits < 3:
            print("Now I hit")
            HoldAndReleaseKey(H, 0.2)
            currentHits += 1;
        else:
            print("Now I stand")
            HoldAndReleaseKey(S, 0.2)

    elif pyautogui.locateOnScreen("bet.png", region=(1600,750,300,300), confidence=0.7) != None:
        print("Now I bet")
        HoldAndReleaseKey(ENTER, 0.2)
        currentHits = 0

    
