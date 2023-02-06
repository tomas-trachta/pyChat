import socket
import threading
from time import sleep
from src.models.data import ServerData
from src.viewmodels.networking.client import Client

class Server(ServerData, Client):

    def __init__(self):

        super().__init__("", False, self.getMyIp(), 2, 443, "utf-8", "!CONN")

        print(self.SERVER)
        self.ADDR = (self.SERVER, self.PORT)

        self.server_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_.bind(self.ADDR)

        serverThread = threading.Thread(target=self.startServer)
        serverThread.start()

    def getMyIp(self):
        return socket.gethostbyname(socket.gethostname())

    def startServer(self):
        self.server_.listen()
        print("listening")
        conn, addr = self.server_.accept()
        print("connected")
        print(addr)
        Client().__init__(True, addr)

        connected = True
        while connected:
            message_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if message_length:
                message_length = int(message_length)
                self.msg = conn.recv(message_length).decode(self.FORMAT)
                self.newMsg = True
                if self.msg == self.DISCONNECT_MESSAGE:
                    connected = False
                    self.msg = "DISCONNECTED"
                    self.newMsg = True
            sleep(0.01)
        conn.close()