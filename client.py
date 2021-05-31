import threading
from mainInterface import MainInterface
from mainInfoReceiver import MainInfoReceiver

class Client:
    def __init__(self):
        mainInterfaceUi = MainInterface()
        self.mainInterfaceUi = mainInterfaceUi

        mainInfoReceiverThread = threading.Thread(target=self.buildMainInfoReceiver, daemon=True)
        mainInfoReceiverThread.start()
        
        mainInterfaceUi.start_root()

    def buildMainInfoReceiver(self):
        mainInfoReceiver = MainInfoReceiver(self.mainInterfaceUi, "main_x", "main_key")

def main():
    client = Client()

if __name__ == "__main__":
    main()
    




     


