import curses
from Car import Robot
from picamera2 import Picamera2
robo = Robot()

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
turn_speed =1
move_speed = 0.4
i =1
try:
    while True:
        #robo.stop()

        char = screen.getch()
        
        
        if char == ord('q'):
            robo.stop()
            break
        elif char == ord('s'):
            robo.stop()
        

        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            robo.right(turn_speed)
            #picam2.capture_file(f"./images/img_{i}_R.jpg")
            i+=1
            
        elif char == curses.KEY_LEFT:
            robo.left(turn_speed)
            #picam2.capture_file(f"./images/img_{i}_L.jpg")
            i+=1
        elif char == curses.KEY_UP:
           robo.forward(move_speed)   
           #picam2.capture_file(f"./images/img_{i}_F.jpg")
                
           i+=1
        elif char == curses.KEY_DOWN:

            robo.backward(move_speed)
        
        
            
finally:
    # shut down cleanly
    picam2.stop()
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
