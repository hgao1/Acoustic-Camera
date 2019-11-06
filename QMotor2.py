# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QMotor2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdN1 = QtWidgets.QLCDNumber(Form)
        self.lcdN1.setObjectName("lcdN1")
        self.gridLayout.addWidget(self.lcdN1, 0, 0, 1, 1)
        self.lcdN2 = QtWidgets.QLCDNumber(Form)
        self.lcdN2.setObjectName("lcdN2")
        self.gridLayout.addWidget(self.lcdN2, 0, 1, 1, 1)
        self.spinN1 = QtWidgets.QSpinBox(Form)
        self.spinN1.setMinimum(-1000)
        self.spinN1.setMaximum(1000)
        self.spinN1.setObjectName("spinN1")
        self.gridLayout.addWidget(self.spinN1, 1, 0, 1, 1)
        self.spinN2 = QtWidgets.QSpinBox(Form)
        self.spinN2.setMinimum(-1000)
        self.spinN2.setMaximum(1000)
        self.spinN2.setObjectName("spinN2")
        self.gridLayout.addWidget(self.spinN2, 1, 1, 1, 1)
        self.pushGo = QtWidgets.QPushButton(Form)
        self.pushGo.setObjectName("pushGo")
        self.gridLayout.addWidget(self.pushGo, 2, 0, 1, 1)
        self.pushQuit = QtWidgets.QPushButton(Form)
        self.pushQuit.setObjectName("pushQuit")
        self.gridLayout.addWidget(self.pushQuit, 2, 1, 1, 1)

        self.retranslateUi(Form)
        self.pushQuit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushGo.setText(_translate("Form", "Go"))
        self.pushQuit.setText(_translate("Form", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
