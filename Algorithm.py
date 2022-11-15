from HealthTracker import HealthTracker
import KeyboardOutput.CommandList as CommandList
import asyncio
import Character
from ObjectDetection import GetImage, ObjectDetection
import config
import cv2
import numpy as np

from asyncio import get_event_loop
import asyncio
import sys
from threading import Thread
import threading
import cv2
import torch
from Character import Character
from Character import Algorithm
from HealthTracker import HealthTracker
from yolov5.utils import *
from torchvision.io import read_image
import numpy as np
from PIL import Image
from mss import mss
import win32gui
import config
import wx
class Algorithm():

    async def algorithm():
        while True:
                CommandList.upLeft()
                await asyncio.sleep(.5)
                CommandList.fbRight()
                await asyncio.sleep(.5)
    


    
    async def checkHit(time, player : Character ):    
        while time > 0: 
            if player.previous_health > player.current_health :
                return True
                
            await asyncio.sleep(.1)
            time - .1
        return False
      
        asyncio.sleep(time)  





def capturePredict(self):
        """
            Captures the Street Fighter window and displays predictions

        """

        imageGetter = ObjectDetection.GetImage(self.bounding_box)
        imageGetter.start()

        while True:
            sct_img = imageGetter.frame
            HealthTracker.updatePlayersHealth(sct_img)
            results = self.model(sct_img)
            
            char1, char2 =  Character.generatePlayers(results.pandas().xyxy[0])
            Character.updatePlayers(char1,char2)
            if not config.player1.empty():
                # print({config.player1.ymax,config.player1.isKnockedDown()})

                Character.updatePlayers(config.player1,config.player2)
            cv2.imshow('screen', np.squeeze(results.render()))
            # asyncio.run(Character.algorithm())
            asyncio.run(Algorithm.checkHit(5, config.player2))
            if (cv2.waitKey(1) == ord('q')  or imageGetter.stopped):
                cv2.destroyAllWindows()
                imageGetter.stop()
                break

print("STARTING")


def main():
    od = ObjectDetection()
    od.capturePredict()


if __name__ == "__main__":
    main()