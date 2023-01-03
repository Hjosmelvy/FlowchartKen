
from threading import Thread
import threading
import cv2
from Character import Character
import numpy as np
from mss import mss
import win32gui
import config
from torch import hub
import torch



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
            
    def stop(self):
        self.stopped = True

class ShowImage(threading.Thread):

    def __init__(self, imageGetter: GetImage):
        self.imageGetter = imageGetter
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv2.imshow("Video", self.imageGetter.frame)

    def stop(self):
        self.stopped = True
 



class ObjectDetection():

# try loading model first then passing it into class, maybe as an array with index 1 or variable
    def __init__(self, model = None, model_bool : bool = True):
        self.game_window = 0
        win32gui.EnumWindows(self.findStreetFighterWindow, None)
        print(self.game_window)
        self.bounding_box = self.getWindowPos(self.game_window)
        self.model_bool = model_bool
        if(model_bool):
            self.model = model
            self.model.eval()
            self.model.max_det = 2



    def findStreetFighterWindow( self, hwnd, ctype ):
        """
        Returns window handle, as int, that contains the game title 
        Must be run as a handler for win32gui.EnumWindows()
        
        hwnd: Window ID as int
        Done this way because win32gui.EnumWindows does not support returning values while looping throught the list of windows
        """
        window_title = win32gui.GetWindowText(hwnd)
        game_name = "Street Fighter III 3rd Strike: Fight for the Future" 
        if game_name in window_title:
            self.game_window = hwnd
            print(win32gui.GetWindowText(hwnd) + " " + "LINE 75")

   
    def getWindowPos(self, hwnd):
        #ToDo: Remove the window menu in the window
        window_box = win32gui.GetWindowRect(hwnd)
        print(window_box)
        x = window_box[0]
        y = window_box[1]
        w = window_box[2] - x
        h = window_box[3] - y
        return({'top': y, 'left': x , 'width': w , 'height': h })
        


    def detect(self, img):
        """ Returns image with detection algorithm results"""
        return self.model(img)

    def capture(self):
        """
            Captures the Street Fighter window without displaying predictions
        """
        imageGetter = GetImage(self.bounding_box).start()
        imageShower = ShowImage(imageGetter).start()
        while True:
            if cv2.waitKey(1) == ord("q"):
                imageShower.stop()
                imageGetter.stop()

 
    def capturePredict(self):
        """
            Captures the Street Fighter window and displays predictions

        """

        imageGetter = GetImage(self.bounding_box)
        imageGetter.start()
        sct_img = imageGetter.frame
        results = self.model(sct_img)
        self.model.cuda()

        char1, char2 =  Character.generatePlayers(results.pandas().xyxy[0])
        Character.updatePlayers(char1,char2)

        while True:
            sct_img = imageGetter.frame
            results = self.model(sct_img, size=640)
            cv2.imshow('screen', np.squeeze(results.render()))

            if (cv2.waitKey(1) == ord('q')  or imageGetter.stopped):
                cv2.destroyAllWindows()
                imageGetter.stop()
                break
            

if __name__ == "__main__":

    model = torch.hub.load('../Object_Detect_Project/yolov5', 'custom',
                            path="../Object_Detect_Project/yolov5/runs/train/exp48/weights/best.pt", source="local", force_reload=True)
    od = ObjectDetection(model)

    od.capturePredict()




