from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtCore import (pyqtSlot, QTimer)
from Polargraph import Motors
from QMotor2 import Ui_Form


class fancy(QWidget):

    def __init__(self):
        super(fancy, self).__init__()
        self.device = Motors()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushGo.clicked.connect(self.getmoving)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDisplay)
        self.delay = 100.
        self.timer.setInterval(self.delay)

    @pyqtSlot()
    def getmoving(self):
        n1 = self.ui.spinN1.value()
        n2 = self.ui.spinN2.value()
        self.device.goto(n1, n2)
        self.timer.start()

    @pyqtSlot()
    def updateDisplay(self):
        n1, n2 = self.device.indexes
        self.ui.lcdN1.display(n1)
        self.ui.lcdN2.display(n2)
        if not self.device.running():
            self.timer.stop()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Form = fancy()
    Form.show()
    sys.exit(app.exec_())
