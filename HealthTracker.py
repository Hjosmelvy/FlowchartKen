from asyncio import get_event_loop
import asyncio
import sys
from threading import Thread
import threading
import cv2
import torch
from Character import Character
from Character import Algorithm
from yolov5.utils import *
from torchvision.io import read_image
import numpy as np
from PIL import Image
from mss import mss
import win32gui
import config
import wx
# Screen capture
# Model



class HealthTracker(threading.Thread):
    def __init__(self, ):
        self.stopped = False
        self.frame = None
        # self.queue = queue
    def setFrame(self, frame):
        self.frame = frame 
    def start(self, frame):
        Thread(target=lambda: self.updatePlayersHealth(frame)).start()
        return self 
    def getHealthPercent(health):
        """
            returns player health as a percent given array with the location of players health bar
        """

        totalHealth = 497     
        filter = np.asarray([[0,195,255,255], [0,251,16,255], [0,251,255,255]])
        # print(filter)
        bool = (health[:,None] == filter).all(-1).any(-1)
        health = health[np.where(bool)]
        np.reshape(health, (4, -1))
        return round(np.shape(health)[0] / totalHealth , 2)

    def updatePlayersHealth(self, frame: np.array):
    
        player1Health = frame[132,33:530]
        player2Health = frame[132,680:1177]

        while not self.stopped:
            config.player1.previous_health = config.player1.current_health
            config.player2.previous_health = config.player2.current_health
            config.player1.current_health = HealthTracker.getHealthPercent(player1Health)
            config.player2.current_health = HealthTracker.getHealthPercent(player2Health)
            print(config.player2.current_health)
    
    # async def hit_event_handler(player : Character, flag : asyncio.Event()):    
        
    #     while True:
    #         if player.previous_health > player.current_health:
    #             flag.set()
    #             break
    # async def checkHit( time, player : Character):
    #     flag = asyncio.Event()

    #     try:
    #         await asyncio.wait_for(HealthTracker.hit_event_handler(player,flag), timeout=time)
    #     except TimeoutError:
    #         print("missed")
    #         return False
    #     print("hit")
    #     return True      

    # async def eternity():
    #     # Sleep for one hour
    #     await asyncio.sleep(3600)
    #     print('yay!')

    # async def test():
    #     # Wait for at most 1 second
    #     try:
    #         await asyncio.wait_for(HealthTracker.eternity(), timeout=1.0)
    #     except TimeoutError:
    #         print('timeout!')


# Expected output:
#
#     timeout!



    # def get(self, frame):
    #     while not self.stopped:
    #         """
    #             rgb(16, 251, 0) = green = 100% health
    #             rgb(255, 251, 0) = yellow = when current health is less than 100%
    #             rgb(255, 195, 0) = yellow orange = when current health is under 25%
    #             total health bar length: 497
    #         """
    #         player1Health = frame[132,33:530]
    #         player2Health = frame[132,680:1177]
            

            
    #         player2hp = self.getHealthPercent(player2Health)
    #         print(player2hp)


    #         self.frame[132:133,33:530] = (0,0,0) #player 1 health
    #         self.frame[132:133,680:1177] = (0,0,0) #player 2 health

    # def stop(self):
    #     self.stopped = True


    