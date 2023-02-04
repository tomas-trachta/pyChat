import socket
import threading
from time import sleep
from src.models.data import ClientData

class Client(ClientData):

    def __init__(self):
        super().__init__(False, "", False, "", None, 2, 443, "utf-8", "!CONN")

        thread1 = threading.Thread(target=self.waitForIp)
        thread1.start()

    def waitForIp(self):
        while True:
            if self.ipSetUp == True:
                self.connect_to_server()
                self.ipSetUp = False
            sleep(0.01)

    def connect_to_server(self):
        print("connecting..")
        self.ADDR = (self._SERVER_, self.PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.client.connect_ex(self.ADDR))
        print("connected")
        while True:
            if self.sendMsg == True and self.client != None:
                self.sendMsg = False
                self.send()
            sleep(0.01)

    def send(self):
        msg = self.message.encode(self.FORMAT)
        msg_length = len(msg)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(msg)
