from mainInfoSensor import MainInfoSensor
import threading

def main():
    mainInfoSensorThread = threading.Thread(target=mainInfoSensor)
    mainInfoSensorThread.start()

def mainInfoSensor():
    mainInfoSensorObj = MainInfoSensor("Sensor1", "Temperatura")

if __name__ == "__main__":
    main()