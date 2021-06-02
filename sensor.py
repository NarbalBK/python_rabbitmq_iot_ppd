from mainInfoSensor import MainInfoSensor
from sensorController import SensorController
from infoSensor import InfoSensor
import threading

class Sensor:
    def __init__(self, nome, tipo, min, max, min_target, max_target, clock):
        self.exchange = "main_x"
        self.nome = nome
        self.tipo = tipo
        self.min = min
        self.max = max
        self.min_target = min_target
        self.max_target = max_target
        self.clock = clock

        mainInfoSensorThread = threading.Thread(target=self.mainInfoSensor)
        mainInfoSensorThread.start()
        buildSensorControllerThread = threading.Thread(target=self.buildSensorController)
        buildSensorControllerThread.start()

    def mainInfoSensor(self):
        mainInfoSensorObj = MainInfoSensor(self.nome, self.tipo, self.exchange, "main_key")

    def buildSensorController(self):
        infoSensorObj = InfoSensor(self.exchange, self.nome+" - "+self.tipo)
        sensorControllerObj = SensorController(infoSensorObj ,self.min, self.max, self.min_target, self.max_target, self.clock)
        

def main():
    sensor = Sensor("Sensor1", "Temperatura", 30, 50, 20, 40, 0.2)

if __name__ == "__main__":
    main()