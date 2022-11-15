from asyncio import get_event_loop
import asyncio
from queue import Queue
import sys
from threading import Thread
import threading
import multiprocessing
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




def getImage(bounding_box, out_queue: Queue):
    sct = mss()
    while True:
        out_queue.put(np.array(sct.grab(bounding_box)))

# class GetImage(multiprocessing.Process):
#     def __init__(self, bounding_box, out_queue: Queue):
#         self.bounding_box = bounding_box
#         self.sct = mss()
#         self.stopped = False
#         self.frame =  np.array(self.sct.grab(self.bounding_box))
#         self.queue = out_queue 

#     def start(self):
#         multiprocessing.Process(target=self.get).start()
    
#     def get(self):
#         while not self.stopped:
#             self.frame = np.array(self.sct.grab(self.bounding_box))
#             self.queue.put(self.frame)

            # if not config.player2.empty():
            #     self.frame = cv2.circle( self.frame, config.player2.midpoint, radius=0, color=(0,255,255), thickness=2)
    # def stop(self):
    #     self.stopped = True


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
   

    # def displayLoop(self, imageGetter : GetImage, healthTracker = HealthTracker):
    #     """
    #         Captures the Street Fighter window without displaying predictions
    #     """
    #     # imageGetter = GetImage(self.bounding_box)
    #     imageGetter.start()
    #     healthTracker.start(imageGetter.frame)

    #     while True:
    #         healthTracker.setFrame(imageGetter.frame)
    #         cv2.imshow('screen', imageGetter.frame)

    #         if (cv2.waitKey(1) == ord('q')  or imageGetter.stopped):
    #             cv2.destroyAllWindows()
    #             imageGetter.stop()
    #             break

    def displayFromQueue(self, queue : Queue):
        """
            Captures the Street Fighter window without displaying predictions
        """
        # imageGetter = GetImage(self.bounding_box)


        while True:
            image =  queue.get(block=True)
            print(image)
            cv2.imshow('screen', image)

            if (cv2.waitKey(1) == ord('q')  ):
                cv2.destroyAllWindows()
                break


    def display( frame):
        cv2.imshow('screen', frame)

    def predict(self, frame):
        return np.squeeze(self.model(frame))


    def main(self):
        input_queue = Queue()
        output_queue = Queue()
        imageGetter = multiprocessing.Process(target=getImage, args=(self.bounding_box, input_queue))
        imageGetter.start()
        self.displayFromQueue(input_queue)

if __name__ == "__main__":

    m = ObjectDetection()
    m.main()

    # def capturePredict(self):
    #     """
    #         Captures the Street Fighter window and displays predictions

    #     """

    #     imageGetter = GetImage(self.bounding_box)
    #     imageGetter.start()
    #     sct_img = imageGetter.frame
    #     results = self.model(sct_img)
    #     char1, char2 =  Character.generatePlayers(results.pandas().xyxy[0])
    #     Character.updatePlayers(char1,char2)
    #     loop = asyncio.get_event_loop()
    #     while True:
    #         sct_img = imageGetter.frame
    #         results = self.model(sct_img)
    #         asyncio.ensure_future(HealthTracker.updatePlayersHealth(sct_img))
    #         if not config.player1.empty():
    #             # print({config.player1.ymax,config.player1.isKnockedDown()})

    #             Character.updatePlayers(config.player1,config.player2)

    #         cv2.imshow('screen', np.squeeze(results.render()))


    #         if (cv2.waitKey(1) == ord('q')  or imageGetter.stopped):
    #             cv2.destroyAllWindows()
    #             imageGetter.stop()
    #             break




            

    

# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# model.to(device)

# bounding_box = {'top': 0, 'left': 0, 'width': 1248, 'height': 896}

# sct = mss()
# while True:
#     sct_img = np.array(sct.grab(bounding_box))

#     result = model(sct_img)
#     result.print()
#     # if result == None:
#     #     result = sct_img

#     cv2.imshow('screen', np.squeeze(result.render()))
#     if (cv2.waitKey(1) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break


# Recording Screen
# while True:
#     sct_img = sct.grab(bounding_box)
#     cv2.imshow('screen', np.array(sct_img))

#     if (cv2.waitKey(1) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break

# results.xyxy[0]  # im1 predictions (tensor)
# results.pandas().xyxy[0]  # im1 predictions (pandas)
# # #      xmin    ymin    xmax   ymax  confidence  class    name
# # # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# # # 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# # # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# # # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie


#          xmin        ymin         xmax        ymax  confidence  class     name
# 0  621.556458  465.093292   874.244751  872.699524    0.967523      9  Chun-Li
# 1  998.945435  423.396118  1203.942261  877.145691    0.930768      9  Chun-Li
# <class 'pandas.core.frame.DatadaaFrame'>