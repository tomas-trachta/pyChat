from src.viewmodels.networking.server import Server
from src.viewmodels.networking.client import Client
from src.models.data import ClientData

class Network(Server,Client):
    def __init__(self):
        Server.__init__(self)
        Client.__init__(self)