import asyncio
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
    time.sleep(.05)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_W.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_A.value)

def upRight():
    CharacterController.pressKey(ScanCode.ScanCode.KEY_W.value)
    CharacterController.pressKey(ScanCode.ScanCode.KEY_D.value)
    time.sleep(.05)

    CharacterController.releaseKey(ScanCode.ScanCode.KEY_W.value)
    CharacterController.releaseKey(ScanCode.ScanCode.KEY_D.value)

def downRight():
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

def downLeft():
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

def dpRight():
    #dragon punch motion forward
    right()
    down()
    downRight()
    time.sleep(.05)
    heavyPunch()


def dpLeft():
    left()
    down()
    downLeft()
    time.sleep(.05)
    heavyPunch()
def qcRight():
    #quarter circle motion forward
    down()
    downRight()
    right()

def qcLeft():
    #quarter circle motion backward
    down()
    downLeft()
    left()


def fbRight():
    qcRight()
    time.sleep(.05)
    heavyPunch()

def fbLeft():
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

