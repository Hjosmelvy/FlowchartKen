
# Flowchart Ken

An impractical application of an internet meme made to learn Yolov5 Object Detection, multiprocessing, and multithreading.
It looks for an instance of Street Fighter III - Third Strike, takes screenshots, processes the images, sends player location and health to a process, and finally uses the information collected to determine what moves to execute.   



## Screenshots

![](/media/detection-results.gif)

## How to run

1. Install Fightcade for Street Fighter III 3rd Strike: Fight For The Future. More information can be found at https://www.fightcade.com/help
2. Map the inputs.
a. paste the file ..\Object_Detect_Project\utils\inputs.ini into ..\Fightcade\emulator\fbneo\config\presets 

b. Open Fightcade, run a training instance of 3rd Strike by pressing the "Training" button near the top right hand corner of the window.

c. After the emulator is launched, press F5.

d. Select "Player 1", "inputs" for the left-most, center-most dropdown menus respectively. 

e. Press the "Use preset" button.

3. run ..\Object_Detect_Project\main.py for algorithm. 
a. run ..\Object_Detect_Project\ObjectDetection.py to view the object detetion results.



