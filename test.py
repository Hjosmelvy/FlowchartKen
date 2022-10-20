import re
import cv2
import torch
from PIL import Image
from yolov5.utils import *
from torchvision.io import read_image
import numpy as np
from PIL import ImageGrab
from PIL import Image
from mss import mss
import win32gui
# Screen capture
# Model
sct = mss()

global game_window
game_window = 0

def winEnumHandler( hwnd, ctx ):
    window_title = win32gui.GetWindowText(hwnd)
    game_name = "Street Fighter III 3rd Strike: Fight for the Future" 
    if game_name in window_title:
        global game_window
        game_window =  hwnd

win32gui.EnumWindows( winEnumHandler, None )
print(game_window)

window_box = win32gui.GetWindowRect(game_window)
x = window_box[0]
y = window_box[1]
w = window_box[2] - x
h = window_box[3] - y
print(x,y,w,h)
# model = torch.hub.load('G:/Object_D+
# etect_Project/yolov5', 'custom',
#                         path="G:/Object_Detect_Project/yolov5/runs/train/exp3/weights/best.pt", source="local", force_reload=True)

# while True:
#     sct_img = cv2.cvtColor(np.array(sct.grab(bounding_box)), cv2.COLOR_RGB2BGR)
#     results = model(sct_img)
#     cv2.imshow('screen', np.squeeze(results.render()))
#     if (cv2.waitKey(1) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break
    

# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# model.to(device)


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
