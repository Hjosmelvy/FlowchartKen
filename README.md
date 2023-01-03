
# Flowchart Ken

An impractical application of an internet meme made to learn Yolov5 Object Detection, multiprocessing, and multithreading.
It looks for an instance of Street Fighter III - Third Strike, takes screenshots, processes the images, sends player location and health to a process, and finally uses the information collected to determine what moves to execute.   



## Gifs

Algorithm in use
![](/media/flowchart-ken.gif)

Detection Results
![](/media/detection-results.gif)

## How to run

1. Install Fightcade for Street Fighter III 3rd Strike: Fight For The Future. More information can be found at https://www.fightcade.com/help
2. Map the inputs.
    1. paste the file ..\Object_Detect_Project\utils\inputs.ini into ..\Fightcade\emulator\fbneo\config\presets 

    2. Open Fightcade, and run a training instance of 3rd Strike by pressing the "Training" button near the top right-hand corner of the window.

    3. After the emulator is launched, press F5.

    4. Select "Player 1" and "inputs" for the left-most, and center-most dropdown menus respectively. 

    3. Press the "Use preset" button.

3. run ..\Object_Detect_Project\main.py for algorithm.
    - Press "Q" to close processes
    - Press the left or right arrow to tell the algorithm which direction your character is

4. (Optional) run ..\Object_Detect_Project\ObjectDetection.py to view the object detetion results.
    - Press "Q" to close the CV2 window.

### Notes:

- The algorithm occasionally requires user input. This can be fixed by retraining the object detection model with 28,000+ more images. Or significantly more effort, time, and effort than want would be appropriate for this project.

- Do not move or change the size of the emulator window while running either file. In case it happens, restart the file you ran.