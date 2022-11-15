    
from HealthTracker import HealthTracker
from ObjectDetection import ObjectDetection
from config import player2
import asyncio

async def main():
    od = ObjectDetection()
    od.capture()
  

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
