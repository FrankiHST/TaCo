from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from extractionClass import Extraktion
import sys

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        button_a = QPushButton('Extraktionen anlegen', self)
        button_a.setFixedSize(250, 50)
        button_a.move(75, 50)
        button_a.setToolTip("Extraktionen aus Konfigurationsdatei anlegen")
        
        button_u = QPushButton('Extraktionen umbenennen', self)
        button_u.setFixedSize(250, 50)
        button_u.move(75, 100)
        button_u.setToolTip("Extraktionen nach gewähltem Namensschema umbenennen")
        #button_u.clicked.connect(self.event)
        
        button_e = QPushButton('Extraktionen einstellen', self)
        button_e.setFixedSize(250, 50)
        button_e.move(75, 150)
        button_e.setToolTip("Extraktionen aus Konfigurationsdatei analog der Konfigurationsdatei einstellen")
        #button_e.clicked.connect(self.close)

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Main Window')
        self.setWindowIcon(QIcon())
        
        self.show()
        
    def startEvent(self, event):
        reply = QMessageBox.question(self, 'Nachricht', "Sollen die Extraktionen angelegt werden?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def fensterStarten(self):
        app = QApplication(sys.argv)
        mainWindow = FirstWindow()
        app.quit
        sys.exit(app.exec_())