from mainInfoSensor import MainInfoSensor
import threading

def main():
    mainInfoSensorThread = threading.Thread(target=mainInfoSensor)
    mainInfoSensorThread.start()

def mainInfoSensor():
    mainInfoSensorObj = MainInfoSensor("Sensor2", "Velocidade", "main_x", "main_key")

if __name__ == "__main__":
    main()