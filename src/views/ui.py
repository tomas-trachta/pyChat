from PySide6.QtWidgets import QTextEdit, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtCore import Signal, Slot
from src.views.mainwindow import MainWindow
from src.viewmodels.data import Data
from src.viewmodels.network import Network
import threading
from time import sleep

class UI(MainWindow, Network, Data):
    update_text_signal = Signal()
    def __init__(self):
        MainWindow.__init__(self)
        Network.__init__(self)
        Data.__init__(self)
        
        self.run()
        self.update_text_signal.connect(self.transferData)

    ##############################################################
    ####################### UI creation ##########################
    ##############################################################
    #region UI creation
    
    def createWidgets(self):
        self.myIp = QLineEdit()
        self.myIp.setReadOnly(True)
        self.myIp.setText("Your IP is: " + self.SERVER)

        self.targetIP = QLineEdit(self)
        self.targetIP.setText("Enter target IP and press <Enter>")
        self.targetIP.returnPressed.connect(self.setUpIp)

        self.chat = QTextEdit(self)
        self.chat.setReadOnly(True)

        self.chatInput = QLineEdit(self)
        self.chatInput.returnPressed.connect(self.addUserData)

    def createLayout(self):
        self.layout_ = QVBoxLayout()

        self.layout_.addWidget(self.myIp)
        self.layout_.addWidget(self.targetIP)
        self.layout_.addWidget(self.chat)
        self.layout_.addWidget(self.chatInput)

        self.centralWidget_ = QWidget(self)
        self.centralWidget_.setLayout(self.layout_)

        self.setCentralWidget(self.centralWidget_)

    def run(self):
        self.createWidgets()
        self.createLayout()
        self.show()
        thread=threading.Thread(target=self.waitForData)
        thread.start()

        
    #endregion
    ##############################################################
    ##############################################################


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
        self.chat.setText("")
        self.chat.setText(self.data.DATA)

    def waitForData(self):
        while True:
            if self.newMsg == True:
                self.data.add(self.msg, 1)
                self.update_text_signal.emit()
                self.newMsg = False
            sleep(0.01)








