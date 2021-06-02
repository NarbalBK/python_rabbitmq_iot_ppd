import math
import time

class SensorController:
    def __init__(self, infoSensor, min, max, min_target, max_target, clock):
        self.on = True
        self.min = min
        self.max = max
        self.clock = clock
        self.min_target = min_target
        self.max_target = max_target
        self.variation = (max-min)
        self.infoSensor = infoSensor
        self.sinFunction()
        
    def sinFunction(self):
        while True:
            for i in range (0,180, 5):
                x=math.sin(math.radians(i))
                x=x*(self.variation)+self.min
                time.sleep(self.clock)
                print(x)
                if x >= self.max_target:
                    self.infoSensor.sendMsg(x)
                elif x<= self.min_target:
                    self.infoSensor.sendMsg(x)


