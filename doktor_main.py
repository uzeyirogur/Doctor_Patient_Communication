from PySide6.QtWidgets import *
from doktor_designer import Ui_DoktorEkrani
from hasta import HastaPage


class HastaneSistemi(QWidget) :
    def __init__(self) :
        super().__init__()
        self.doktor = Ui_DoktorEkrani()
        self.doktor.setupUi(self)
        self.hasta = HastaPage()
        self.hasta.show()
        self.hasta.hastasinyali.connect(self.HastaBilgi)
        self.doktor.pushButton_doktor.clicked.connect(self.DoktorBilgi)
    def HastaBilgi(self,bilgi) :
        self.doktor.label_2_doktorbilgi.setText(bilgi)

    def DoktorBilgi(self) :
        doktorbilgi = self.doktor.textEdit_doktor_mesaj.toPlainText()
        self.hasta.hastaformu.label_2_hastabilgi.setText(doktorbilgi)

app = QApplication([])
pencere = HastaneSistemi()
pencere.show()
app.exec()