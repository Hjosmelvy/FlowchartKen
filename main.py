import ctypes
import threading
from Character import Character
import config
from HealthTrackerProcess import HealthTracker, HitCheck
import multiprocessing  as mp
import torch
from time import sleep
from multiprocessing.connection import PipeConnection
from KeyboardOutput import CommandList
from ObjectDetection import ObjectDetection
import numpy as np
from random import randint

import keyboard as kb
class Algorithm(mp.Process):
    def __init__(self, recieve_conn : PipeConnection, send_conn : PipeConnection , healthTracker, isRunning, side):
        mp.Process.__init__(self)
        self.recieve_conn = recieve_conn
        self.send_conn = send_conn
        self.healthTracker = healthTracker
        self.isRunning = isRunning
        self.side = side
    def run(self):
        while self.isRunning.value:
            x= bool(self.side.value)
            if randint(0,1):
                CommandList.upLeft(x)
                sleep(.49)
                self.hadouken_loop(x)
            else:
                x = bool(self.side.value)
                HitCheck(self.healthTracker.player2_event, self.send_conn, 1.25).start() 
                CommandList.upRight(x)
                sleep(.45)
                CommandList.heavyKick()
                hitcheck = self.recieve_conn.recv()
                if(not hitcheck):
                    continue
          
            CommandList.dpRight(x)
            sleep(1.5)

    def hadouken_loop(self, reverse : bool = False):
        while True: 
            CommandList.fbRight(reverse)
            HitCheck(self.healthTracker.player2_event, self.send_conn, 1).start()
            if(self.recieve_conn.recv()):
                #enemy has taken any damage from hadouken
                sleep(.5)
                pass
            else:
                break

class Detect(threading.Thread): #produces empty dataframes if Process instead of Threading
    #this is needed to update characters' location
    def __init__(self, in_queue : mp.Queue, out_queue : mp.Queue, model,isRunning ):
        threading.Thread.__init__(self)
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.model = model
        self.isRunning = isRunning


    def run(self):
        while self.isRunning.value:
            frame =  self.in_queue.get()
            self.out_queue.put(frame) 

            x = self.model(np.asarray(frame)).pandas().xyxy[0].sort_values('xmin')
            char1, char2 = Character.generatePlayers(x)
            Character.updatePlayers(char1, char2)

class KeyboardListener(mp.Process):
    def __init__(self, isRunning, side):
        mp.Process.__init__(self)
        self.isRunning = isRunning
        self.side  = side 
    def run(self):
        while self.isRunning:
            event = kb.read_event()
            if event.event_type == kb.KEY_DOWN:
                if event.name == "q":
                    self.isRunning.value = False
                    print("Ending all Processes...", flush=True)
                    return
                if event.name == 'left':
                    self.side.value = 0
                    print("///////////////////////////////")
                if event.name  == "right": 
                    self.side.value = 1
                    print("///////////////////////////////")
  
class Grabber(mp.Process):
    def __init__(self,queue : mp.Queue, size, isRunning):
        mp.Process.__init__(self)
        self.queue = queue
        self.size = size
        self.isRunning = isRunning

    def run(self):
        from mss import mss
        with mss() as sct:
            while self.isRunning.value:
                self.queue.put(sct.grab(self.size))
            
def main():
    model = torch.hub.load('G:/Object_Detect_Project/yolov5', 'custom',
                            path="G:/Object_Detect_Project/yolov5/runs/train/exp48/weights/best.pt", source="local", force_reload=True)
    od = ObjectDetection(model)
    q1 = mp.SimpleQueue()
    q2 = mp.SimpleQueue()
    out_pipe, in_pipe = mp.Pipe()

    running = mp.Value(ctypes.c_bool, True)
    grabber = Grabber(q1, od.bounding_box, running)
    detect = Detect(q1, q2, model, running)
    health  = HealthTracker(running, q2)
    algorithm = Algorithm(out_pipe, in_pipe, health, running, config.player1.side)
    
    grabber.start()
    detect.start()
    algorithm.start()
    health.start()

    KeyboardListener(running, config.player1.side).start()
          

if __name__ == "__main__":
    main()
