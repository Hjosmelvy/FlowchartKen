
import ctypes
from multiprocessing import Process, Value, Queue, Event, connection

from threading import Thread
import numpy as np
import config


class HitCheck(Thread):
    """ Handles hit events when running"""
    def __init__(self, event: Event,  conn2 : connection.Connection, timeout : int):
        Thread.__init__(self)
        self.conn2 = conn2
        self.e = event
        self.timeout = timeout
    
    def run(self):
        if(self.e.is_set()):
            self.e.clear()
        result = self.e.wait(timeout = self.timeout)
        print(f"Hit?: {result}")
        self.conn2.send(result)
        return 

class HealthTracker(Process):
    def __init__(self, running, queue : Queue  = None ):
        Process.__init__(self)
        # self.player1_current_health = Value(ctypes.c_double, 1)
        # self.player2_current_health = Value(ctypes.c_double, 1)
        # self.player1_prev_health = Value(ctypes.c_double, 1)
        # self.player2_prev_health = Value(ctypes.c_double, 1)
        self.queue = queue
        self.player1_event = Event()
        self.player2_event = Event() 
        self.running = running
    def run(self):
        while self.running:
            frame = self.queue.get()
            self.updatePlayersHealth(np.asarray(frame))

    def getHealthPercent(health):
        """
            returns player health as a percentage given array with the location of players health bar
        """
        #Reads RGBA values of a line of pixels going across the full length of the health bar
        #health bar goes from green to orange as it gets depleted. 
        #filter out colors that arent the health bar 
        #return remaining array size divided by max health bar pixel width.  
        totalHealth = 497                           
        filter = np.asarray([[0,195,255,255], [0,251,16,255], [0,251,255,255]]) # RGBA values of colors that can appear
        bool = (health[:,None] == filter).all(-1).any(-1) # list of bools, each index states if its corresponding index in health is in filter
        health = health[np.where(bool)] # removes all colors not in filter
        np.reshape(health, (4, -1))
        return round(np.shape(health)[0] / totalHealth , 2)

    def updatePlayersHealth(self, frame: np.array):
        #list of RGBA values of the horizontal center of player1's healthbar
        player1Health = frame[132,33:530]
        player2Health = frame[132,680:1177]
        
        config.player2.prev_health.value = config.player2.current_health.value
        config.player1.current_health.value = HealthTracker.getHealthPercent(player1Health)
        config.player2.current_health.value = HealthTracker.getHealthPercent(player2Health)
        
        if(config.player1.prev_health.value > config.player1.current_health.value):
            self.player1_event.set()
        if(config.player2.prev_health.value > config.player2.current_health.value):
            self.player2_event.set()
