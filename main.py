    
from HealthTracker import HealthTracker
from ObjectDetection import ObjectDetection
from config import player2
import asyncio

def main():
    od = ObjectDetection()
    od.capturePredict()


if __name__ == "__main__":
    main()
