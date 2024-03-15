import curses
from Robot import Robot
robo = Robot()

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            robo.stop()
            break
        elif char == ord('s'):
            robo.stop()
        

        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            robo.right()
        elif char == curses.KEY_LEFT:
            robo.left()      
        elif char == curses.KEY_UP:
           robo.forward()       
        elif char == curses.KEY_DOWN:
            robo.backward()
            
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
