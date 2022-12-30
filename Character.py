from math import sqrt
import pandas
import ctypes
from multiprocessing import Event,  Value


class Character():
    prev_health = Value(ctypes.c_double, 1)
    current_health = Value(ctypes.c_double, 1)
    health_location = None 
    hit_event = Event()
    @staticmethod
    def distance(p1, p2):  
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def __init__(self, dataframe = pandas.DataFrame()):
        if  dataframe.empty:

            self.xmin = 0
            self.ymin = 0
            self.xmax = 0
            self.ymax = 0
            self.name = ""
            self.midpoint = (0, 0)
            self.dataframe = dataframe

         
        else:
            self.xmin, self.ymin, self.xmax, self.ymax, confidence, _class, self.name = dataframe
            self.midpoint = self.calculate_midpoint()
            self.dataframe = dataframe

        self.side = Value("i", 1)  # which side the character is facing

            

    def calculate_midpoint(self):
        x = (self.xmin + self.xmax) / 2
        y = (self.ymin + self.ymax) / 2
        return (x, y)

    def isKnockedDown(self):
        if self.ymax < 740:
            return True
        return False

    def isAirborn(self):
        if self.ymin < 360:
            return True
        return False

    def isRightSide(self, otherPlayer):
        # compares other charater's position to determine if the character calling this method is on the right side
        if (not self.empty() and not otherPlayer.empty()):
            if self.midpoint > otherPlayer.midpoint:
                print("RIGHT SIDE")
                return True
            print("LEFT SIDE")
            return False
        return None
    def empty(self):
        return self.dataframe.empty

    @staticmethod
    def generatePlayers(dataframe: pandas.core.frame.DataFrame):
        p1 = Character()
        p2 = Character()
        if dataframe.shape[0] >= 2:
            p1 = Character(dataframe.iloc[0])
            p2 = Character(dataframe.iloc[1])
        elif dataframe.shape[0] == 1:
            p1 = Character(dataframe.iloc[0])

        return p1, p2
    @staticmethod
    def getLocationData(dataframe : pandas.core.frame.DataFrame):
        char1, char2 = Character.generatePlayers(dataframe.pandas().xyxy[0])

        return char1, char2 
    @staticmethod
    def updatePlayers(char1, char2):
        import config as config
        if(char1.empty() or char2.empty()):
            pass

        elif Character.distance(config.player1.midpoint, char1.midpoint) < Character.distance(config.player1.midpoint, char2.midpoint):
            # returns true if the current player1 midpoint is closer to the previous known location of player1
            # this is needed because the object detection results arent consistant on which player is detected first thus this ensures player location integrity.
            config.player1 = char1
            config.player2 = char2
        else:
            config.player1 = char2
            config.player2 = char1





        

