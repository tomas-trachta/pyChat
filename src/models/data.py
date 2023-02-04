from dataclasses import dataclass

class ChatData:

    def __init__(self):
        self.DATA = ""

    def add(self, data : str, chatter : int):
        if chatter == 0:
            self.DATA += "You: " + data + "\n"

        else:
            self.DATA += "Chatter :" + data + "\n"

    def delete(self):
        self.DATA = ""

@dataclass
class ServerData:
    msg : str
    newMsg : bool
    SERVER : str
    HEADER : int
    PORT : int
    FORMAT : str
    DISCONNECT_MESSAGE : str


@dataclass
class ClientData:
    ipSetUp : bool
    _SERVER_ : str
    sendMsg : bool
    message : str
    client : None
    HEADER : int
    PORT : int
    FORMAT : str
    DISCONNECT_MESSAGE : str