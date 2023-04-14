from PySide6.QtWidgets import QTextBrowser, QLineEdit, QVBoxLayout, QWidget
from src.view.mainwindow import MainWindow

class UI(MainWindow):
    def __init__(self):
        MainWindow.__init__(self)        
        self.run()

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

        self.chat = QTextBrowser(self)

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
        
    #endregion
    ##############################################################
    ##############################################################