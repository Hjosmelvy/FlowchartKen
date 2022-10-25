import KeyboardOutput.CharacterController as CharacterController
import KeyboardOutput.ScanCode as ScanCode
import time

#
#   The methods below assume the character is facing right
#


def heavyPunch():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_NUMPAD9.value)
def jump():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_W.value)

def left():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_A.value)

# def left(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)


def right():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_D.value)

# def right(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)


def down():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_S.value)

# def down(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)


def upLeft():
    CharacterController.pressKey(ScanCode.ScanCode.KEY_W.value)
    CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_W.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)

def upRight():
    CharacterController.pressKey(ScanCode.ScanCode.KEY_W.value)
    CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_W.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)

def downForward():
    CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
    CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
    time.sleep(.01)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)

# def downForward(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)

def downBack():
    CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
    CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
    time.sleep(.01)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)

# def downBack(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)

def dpForward():
    #dragon punch motion forward
    right()
    down()
    downForward()
    time.sleep(.01)
    heavyPunch()


def dpBackward():
    left()
    down()
    downBack()
    time.sleep(.01)
    heavyPunch()
def qcForward():
    #quarter circle motion forward
    down()
    downForward()
    right()

def qcBackward():
    #quarter circle motion backward
    down()
    downBack()
    left()
    # time.sleep(.01)

def fbForward():
    qcForward()
    time.sleep(.01)

    heavyPunch()

def fbBackward():
    qcBackward()
    time.sleep(.01)
    heavyPunch()
