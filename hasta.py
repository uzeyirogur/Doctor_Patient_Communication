from PySide6.QtWidgets import *
from hasta_designer import Ui_HastaEkrani
from PySide6.QtCore import Signal

class HastaPage(QWidget) :
    hastasinyali = Signal(str)
    def __init__(self) :
        super().__init__()
        self.hastaformu = Ui_HastaEkrani()
        self.hastaformu.setupUi(self)
        self.hastaformu.pushButton_hasta.clicked.connect(self.HastaMesaj)


    def HastaMesaj(self) :
        bilgi = self.hastaformu.textEdit_hasta_mesaj.toPlainText()
        self.hastasinyali.emit(bilgi)

