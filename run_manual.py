import curses
from Robo import Robot
from picamera2 import Picamera2
robo = Robot()
import cv2

picam2 = Picamera2()

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)
config = picam2.create_still_configuration()
picam2.configure(config)
picam2.start()
turn_speed = 0.3
move_speed =  0.2

def write_to_disk(data):

    for image , direction, index in data:
        cv2.imwrite( f"./images/img_{index}_{direction}.jpg", image)

i =1
data = []
try:
    while True:
        #robo.stop()
        char = screen.getch()
        
        if char == ord('r'):
            robo.stop()
            print("write in progress...")
            write_to_disk(data)
            data= []
            print("write completed...")

        elif char == ord('q'):
            robo.stop()
            break
        elif char == ord('s'):
            robo.stop()
        
        image = picam2.capture_array()
        if char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            robo.right(turn_speed)
            data.append((image,"R", i))
        elif char == curses.KEY_LEFT:
            robo.left(turn_speed)
            data.append((image,"L", i))
        elif char == curses.KEY_UP:
           robo.forward(move_speed)
           data.append((image,"F", i))
        elif char == curses.KEY_DOWN:
            robo.backward(move_speed)
        i+=1
            
finally:
    # shut down cleanly
    picam2.stop()
    robo.stop()
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
