import threading
from mainInterface import MainInterface
from mainInfoReceivier import MainInfoReceivier

class Client:
    def __init__(self):
        mainInterfaceUi = MainInterface()
        self.mainInterfaceUi = mainInterfaceUi

        mainInfoReceiverThread = threading.Thread(target=self.buildMainInfoReceiver, daemon=True)
        mainInfoReceiverThread.start()
        
        mainInterfaceUi.start_root()

    def buildMainInfoReceiver(self):
        mainInfoReceivier = MainInfoReceivier(self.mainInterfaceUi)

def main():
    client = Client()

if __name__ == "__main__":
    main()
    




     


