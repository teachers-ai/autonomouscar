import gpiod
import time


class Robot:
    def __init__(self, lm_pin1=17, lm_pin2=27, rm_pin1=22, rm_pin2=23):
        self.chip = gpiod.Chip('gpiochip4')
       
        self.lm1 = self.chip.get_line(lm_pin1)
        self.lm2  = self.chip.get_line(lm_pin2)
        self.rm1 = self.chip.get_line(rm_pin1)
        self.rm2  = self.chip.get_line(rm_pin2)
        self.lm1.request(consumer="motor", type=gpiod.LINE_REQ_DIR_OUT)
        self.lm2.request(consumer="motor", type=gpiod.LINE_REQ_DIR_OUT)
        self.rm1.request(consumer="motor", type=gpiod.LINE_REQ_DIR_OUT)
        self.rm2.request(consumer="motor", type=gpiod.LINE_REQ_DIR_OUT)
        self.stop()
        
    def forward(self):
        self.lm1.set_value(0)
        self.lm2.set_value(1)
        self.rm1.set_value(0)
        self.rm2.set_value(1)

    def stop(self):
        self.lm1.set_value(0)
        self.lm2.set_value(0)
        self.rm1.set_value(0)
        self.rm2.set_value(0)

    def backward(self):
        self.lm1.set_value(1)
        self.lm2.set_value(0)
        self.rm1.set_value(1)
        self.rm2.set_value(0)


    def left(self):
        self.lm1.set_value(1)
        self.lm2.set_value(0)
        self.rm1.set_value(0)
        self.rm2.set_value(1)

    def right(self):
            self.lm1.set_value(0)
            self.lm2.set_value(1)
            self.rm1.set_value(1)
            self.rm2.set_value(0)




robo = Robot()
robo.forward()


