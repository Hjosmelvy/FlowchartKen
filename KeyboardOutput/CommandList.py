import asyncio
import KeyboardOutput.CharacterController as CharacterController
import KeyboardOutput.ScanCode as ScanCode
import time

#
#   The methods below assume the character is facing right
#


def heavyPunch():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_NUMPAD9.value)
def heavyKick():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_NUMPAD6.value)
def jump():
    CharacterController.tapKey(ScanCode.ScanCode.KEY_W.value)

def left(reverse : bool = False):
    if reverse:
        right()
    else:
        CharacterController.tapKey(ScanCode.ScanCode.KEY_A.value)

# def left(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)


def right(reverse : bool = False):
    if reverse:
        left()
    else: 
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


def upLeft(reverse : bool = False):
    if reverse:
        upRight()
    else: 
        CharacterController.pressKey(ScanCode.ScanCode.KEY_W.value)
        CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
        time.sleep(.05)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_W.value)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)

def upRight(reverse : bool = False):
    if reverse:
        upLeft()
    else:
        CharacterController.pressKey(ScanCode.ScanCode.KEY_W.value)
        CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
        time.sleep(.05)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_W.value)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)

def downRight(reverse : bool = False):
    if reverse:
        downLeft()
    else:
        CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
        CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
        time.sleep(.05)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)

# def downForward(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)

def downLeft(reverse : bool = False):
    if reverse: 
        downRight()
    else:
        CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
        CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
        time.sleep(.05)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
        CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)

# def downBack(seconds:int):
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.pressKey(ScanCode.ScanCode.KEY_A.value)
#     time.sleep(seconds)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_S.value)
#     CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)

def dpRight(reverse : bool = False):
    #dragon punch motion forward
    if reverse:
        dpLeft()
    else:
        right()
        down()
        downRight()
        time.sleep(.05)
        heavyPunch()


def dpLeft(reverse : bool = False):
    if reverse:
        dpRight()
    else:
        left()
        down()
        downLeft()
        time.sleep(.05)
        heavyPunch()
def qcRight(reverse : bool = False):
    #quarter circle motion forward
    if reverse:
        qcLeft()
    else:
        down()
        downRight()
        right()

def qcLeft(reverse : bool = False):
    #quarter circle motion backward
    if reverse:
        qcRight()
    else:
        down()
        downLeft()
        left()


def fbRight(reverse : bool = False):
    if reverse:
        fbLeft()
    else:
        qcRight()
        time.sleep(.05)
        heavyPunch()

def fbLeft(reverse : bool = False):
    if reverse:
        fbRight()
    else:
        qcLeft()
        time.sleep(.05)
        heavyPunch()

async def test():
    while True:
        dpLeft()
        await asyncio.sleep(1)

        upRight()
        await asyncio.sleep(0.81)

        upLeft()
        await asyncio.sleep(0.81)


if __name__ == '__main__':

    asyncio.run(test())

