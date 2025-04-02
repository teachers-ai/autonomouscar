from Robo import Robot
from picamera2 import Picamera2
from engine import Engine
import cv2
import time
import numpy as np
import threading
import sys


def writetodisk(data):
    for img , direction, index in data:
        filename = f"./predictlogs/{index}_img_{direction}.jpg"
        cv2.imwrite(filename, img)

print(sys.argv)

modelpath = "hanuman1.h5"

if len(sys.argv) >1:
    modelpath = sys.argv[-1]

engine = Engine(modelpath)
robo = Robot()
picam2 = Picamera2()
data = []
config = picam2.create_still_configuration()
picam2.configure(config)
picam2.start()
turn_speed =0.6
move_speed = 0.6
index =1

try:
    while True:
        starttime = time.time()
        #robo.stop()       
        image = picam2.capture_array()
        direction = engine.predict(image)
        data.append((image, direction, index))
        print(direction)
        print(f"total time to predict {time.time()-starttime}")
        if direction == "L":
           robo.left(turn_speed)  

        elif direction == "R":
            robo.right(turn_speed)

        else:
            robo.forward(move_speed)

        if len(data) >100:
           st = time.time()
           data_copy = data[:]
           data = []
           x = threading.Thread(target=writetodisk, args=(data_copy,))
           x.start()
           print(f"time to start thred {time.time()-st}")
          #time.sleep(0.4)
        index+=1
        

finally:
    # shut down cleanly
    print("cleaning.....")
    picam2.stop()
    robo.stop()
    writetodisk(data)


