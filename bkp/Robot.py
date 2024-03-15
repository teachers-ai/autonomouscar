import gpiod
import time
from gpiod.line import Direction, Value

class Robot:
    def __init__(self, lm_pin1=17, lm_pin2=27, rm_pin1=22, rm_pin2=23):

        self.lm_pin1 = lm_pin1
        self.lm_pin2 = lm_pin2
        self.rm_pin1 = rm_pin1
        self.rm_pin2 = rm_pin2
        self.stop()
        
    def forward(self):

        self.requestline(self.lm_pin1, Value.INACTIVE)
        self.requestline(self.lm_pin2, Value.ACTIVE)
        self.requestline(self.rm_pin1, Value.INACTIVE)
        self.requestline(self.rm_pin2, Value.ACTIVE)


    def stop(self):
        self.requestline(self.lm_pin1, Value.INACTIVE)
        self.requestline(self.lm_pin2, Value.INACTIVE)
        self.requestline(self.rm_pin1, Value.INACTIVE)
        self.requestline(self.rm_pin2, Value.INACTIVE)
       

    def backward(self):
        self.requestline(self.lm_pin1, Value.ACTIVE)
        self.requestline(self.lm_pin2, Value.INACTIVE)
        self.requestline(self.rm_pin1, Value.ACTIVE)
        self.requestline(self.rm_pin2, Value.INACTIVE)
      


    def left(self):

        self.requestline(self.lm_pin1, Value.INACTIVE)
        self.requestline(self.lm_pin2, Value.INACTIVE)
        self.requestline(self.rm_pin1, Value.INACTIVE)
        self.requestline(self.rm_pin2, Value.ACTIVE)
      

    def right(self):

        self.requestline(self.lm_pin1, Value.INACTIVE)
        self.requestline(self.lm_pin2, Value.ACTIVE)
        self.requestline(self.rm_pin1, Value.INACTIVE)
        self.requestline(self.rm_pin2, Value.INACTIVE)
       

    def requestline(self, linenum, output):

            with gpiod.request_lines(   "/dev/gpiochip4",  consumer="motor", config={
            linenum: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value= output
            )
        }  ) as request:
       
                    request.set_value(linenum, output)
            

robo = Robot()
robo.stop()

