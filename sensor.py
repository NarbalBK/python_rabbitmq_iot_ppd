from mainInfoSensor import MainInfoSensor
from sensorController import SensorController
from infoSensor import InfoSensor
import threading

def main():
    #TODO CRIAR UMA CLASSE QUE INSTANCIA ESTA FUNCAO E VARIA SEUS VALORES 
    #TODO INSTANCIAR INFO SENSOR
    mainInfoSensorThread = threading.Thread(target=mainInfoSensor)
    mainInfoSensorThread.start()
    buildSensorControllerThread = threading.Thread(target=buildSensorController)
    buildSensorControllerThread.start()


def mainInfoSensor():
    mainInfoSensorObj = MainInfoSensor("Sensor1", "Temperatura", "main_x", "main_key")

def buildSensorController():
    sensorControllerObj = SensorController(2, 45, 0.2)

def buildInfoSensor():
    infoSensorObj = InfoSensor("main_x") #TODO PASSAR O VALOR AQUI OU DENTRO DA FUNCAO


if __name__ == "__main__":
    main()