from KeyboardOutput import CharacterController 
from KeyboardOutput import ScanCode
import time

#
#   The methods below assume the character is facing right
#

def jump():
    CharacterController.tapKey(ScanCode.KEY_W.value)

def left():
    CharacterController.tapKey(ScanCode.KEY_A.value)

def left(seconds:int):
    CharacterController.pressKey(ScanCode.KEY_A.value)
    time.sleep(seconds)
    CharacterController.releaseKey(ScanCode.KEY_A.value)


def right():
    CharacterController.tapKey(ScanCode.KEY_D.value)

def right(seconds:int):
    CharacterController.pressKey(ScanCode.KEY_D.value)
    time.sleep(seconds)
    CharacterController.releaseKey(ScanCode.KEY_D.value)


def down():
    CharacterController.tapKey(ScanCode.KEY_S.value)

def down(seconds:int):
    CharacterController.pressKey(ScanCode.KEY_S.value)
    time.sleep(seconds)
    CharacterController.releaseKey(ScanCode.KEY_S.value)


def upLeft():
    CharacterController.pressKey(ScanCode.KEY_W.value)
    CharacterController.pressKey(ScanCode.KEY_A.value)
    CharacterController.releaseKey(ScanCode.KEY_W.value)
    CharacterController.releaseKey(ScanCode.KEY_A.value)

def upRight():
    CharacterController.pressKey(ScanCode.KEY_W.value)
    CharacterController.pressKey(ScanCode.KEY_D.value)
    CharacterController.releaseKey(ScanCode.KEY_W.value)
    CharacterController.releaseKey(ScanCode.KEY_D.value)

def downForward():
    CharacterController.pressKey(ScanCode.KEY_S.value)
    CharacterController.pressKey(ScanCode.KEY_D.value)
    CharacterController.releaseKey(ScanCode.KEY_S.value)
    CharacterController.releaseKey(ScanCode.KEY_D.value)

def downForward(seconds:int):
    CharacterController.pressKey(ScanCode.KEY_S.value)
    CharacterController.pressKey(ScanCode.KEY_D.value)
    time.sleep(seconds)
    CharacterController.releaseKey(ScanCode.KEY_S.value)
    CharacterController.releaseKey(ScanCode.KEY_D.value)

def downBack():
    CharacterController.pressKey(ScanCode.KEY_S.value)
    CharacterController.pressKey(ScanCode.KEY_A.value)
    CharacterController.releaseKey(ScanCode.KEY_S.value)
    CharacterController.releaseKey(ScanCode.KEY_A.value)

def downBack(seconds:int):
    CharacterController.pressKey(ScanCode.KEY_S.value)
    CharacterController.pressKey(ScanCode.KEY_A.value)
    time.sleep(seconds)
    CharacterController.releaseKey(ScanCode.KEY_S.value)
    CharacterController.releaseKey(ScanCode.KEY_A.value)

def dpForward():
    #dragon punch motion forward
    right()
    down()
    downForward()


def dpBackward():
    #dragon punch motion backwards
    left()
    down()
    downBack()

def qcForward():
    #quarter circle motion forward
    down()
    downForward()
    right()

def qcForward():
    #quarter circle motion backward
    down()
    downBack()
    left()