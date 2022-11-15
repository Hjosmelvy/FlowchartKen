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
# Screen capture
# Model



class GetImage(threading.Thread):
    def __init__(self, bounding_box):
        self.bounding_box = bounding_box
        self.sct = mss()
        self.stopped = False
        self.frame =  np.array(self.sct.grab(self.bounding_box))
    def start(self):
        Thread(target=self.get, args=()).start()
        return self
    def get(self):
        while not self.stopped:
            self.frame = np.array(self.sct.grab(self.bounding_box))
            
            # if not config.player2.empty():
            #     self.frame = cv2.circle( self.frame, config.player2.midpoint, radius=0, color=(0,255,255), thickness=2)
    def stop(self):
        self.stopped = True

class SideSelectInput(threading.Thread):
    def __init__(self, bounding_box):
        self.bounding_box = bounding_box
        self.sct = mss()
        self.stopped = False
        self.frame =  np.array(self.sct.grab(self.bounding_box))
    def start(self):
        Thread(target=self.get, args=()).start()
        return self
    def get(self):
        while not self.stopped:
            key = cv2.waitKey(0)
            if(key == ord(2)):
                #if left arrow key is press 
                 
                pass
            elif(key == ord(3)):
                #if right arrow key is press
                pass   
                
            # if not config.player2.empty():
            #     self.frame = cv2.circle( self.frame, config.player2.midpoint, radius=0, color=(0,255,255), thickness=2)
    def stop(self):
        self.stopped = True






class ObjectDetection:
    model = torch.hub.load('G:/Object_Detect_Project/yolov5', 'custom',
                        path="G:/Object_Detect_Project/yolov5/runs/train/exp48/weights/best.pt", source="local", force_reload=True)
    sct = mss()

    bounding_box = {'top': 0, 'left': 0, 'width': 1248, 'height': 896}

    def findStreetFighterWindow( self, hwnd, ctype ):
        """
        Returns window handle, as int, that contains the game title 
        Must be run as a handler for win32gui.EnumWindows()

        Done this way because win32gui.EnumWindows does not support returning values while looping throught the list of windows
        """
        window_title = win32gui.GetWindowText(hwnd)
        game_name = "Street Fighter III 3rd Strike: Fight for the Future" 
        if game_name in window_title:
            self.game_window = hwnd
            print(win32gui.GetWindowText(hwnd))

   

    def getWindowPos(self, hwnd):
        #ToDo: Remove the window menu in the window
        window_box = win32gui.GetWindowRect(hwnd)
        print(window_box)
        x = window_box[0]
        y = window_box[1]
        w = window_box[2] - x
        h = window_box[3] - y
        return({'top': y, 'left': x , 'width': w , 'height': h })
        
    def __init__(self):
        self.game_window = 0
        win32gui.EnumWindows(self.findStreetFighterWindow, None)
        print(self.game_window)
        self.bounding_box = self.getWindowPos(self.game_window)
   

    def capture(self):
        """
            Captures the Street Fighter window without displaying predictions
        """
        imageGetter = GetImage(self.bounding_box)
        imageGetter.start()
        while True:
            cv2.imshow('screen', imageGetter.frame)

            if (cv2.waitKey(1) == ord('q')  or imageGetter.stopped):
                cv2.destroyAllWindows()
                imageGetter.stop()
                break
            
    def capturePredict(self):
        """
            Captures the Street Fighter window and displays predictions

        """

        imageGetter = GetImage(self.bounding_box)
        imageGetter.start()
        sct_img = imageGetter.frame
        results = self.model(sct_img)
        char1, char2 =  Character.generatePlayers(results.pandas().xyxy[0])
        Character.updatePlayers(char1,char2)
        # ht = HealthTracker()

        while True:
            sct_img = imageGetter.frame
            results = self.model(sct_img)
            HealthTracker.updatePlayersHealth(sct_img)

            if not config.player1.empty():
                # print({config.player1.ymax,config.player1.isKnockedDown()})

                Character.updatePlayers(config.player1,config.player2)

            cv2.imshow('screen', np.squeeze(results.render()))

            asyncio.run(HealthTracker.checkHit(3, config.player2))

            if (cv2.waitKey(1) == ord('q')  or imageGetter.stopped):
                cv2.destroyAllWindows()
                imageGetter.stop()
                break





