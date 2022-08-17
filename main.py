import cv2
import os

FOLDER_NAME = "POSITIVE"

START_POINT = (190,80)
END_POINT = (450,398)

camera = cv2.VideoCapture(0)
count = 0

def createFolder():
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print(f"{FOLDER_NAME} folder created!")
