from src.model.data import ChatData
from src.controller.networking.server import Server
from src.controller.networking.client import Client
from src.model.data import ChatData
from src.view.ui import UI
from PySide6.QtCore import Signal, Slot
from time import sleep
import threading

class AppController(Server,Client,UI):
    update_text_signal = Signal()

    def __init__(self):
        self.data = ChatData()
        Server.__init__(self)
        Client.__init__(self)
        UI.__init__(self)

        thread=threading.Thread(target=self.waitForData)
        thread.start()
        self.update_text_signal.connect(self.transferData)

    def setUpIp(self):
        self._SERVER_ = self.targetIP.text()
        self.ipSetUp = True
        self.targetIP.setText("") 

    def addUserData(self):
        self.data.add(self.chatInput.text(), 0)
        self.message = self.chatInput.text()
        self.chatInput.setText("")
        self.update_text_signal.emit()

        self.sendMsg = True

    @Slot()
    def transferData(self):
        self.chat.setText(self.data.DATA)
        self.chat.verticalScrollBar().setValue(self.chat.verticalScrollBar().maximum())

    def waitForData(self):
        while True:
            if self.newMsg == True:
                self.data.add(self.msg, 1)
                self.update_text_signal.emit()
                self.newMsg = False
            sleep(0.01)
