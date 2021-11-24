# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'predict.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 60, 571, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 90, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(30, 60, 151, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.knn_Button = QtWidgets.QRadioButton(self.widget)
        self.knn_Button.setChecked(True)
        self.knn_Button.setObjectName("knn_Button")
        self.verticalLayout.addWidget(self.knn_Button)
        self.SVM_Button = QtWidgets.QRadioButton(self.widget)
        self.SVM_Button.setObjectName("SVM_Button")
        self.verticalLayout.addWidget(self.SVM_Button)
        self.NN_Button = QtWidgets.QRadioButton(self.widget)
        self.NN_Button.setObjectName("NN_Button")
        self.verticalLayout.addWidget(self.NN_Button)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(30, 290, 102, 24))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.widget2 = QtWidgets.QWidget(self.frame)
        self.widget2.setGeometry(QtCore.QRect(30, 340, 168, 24))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.widget3 = QtWidgets.QWidget(self.frame)
        self.widget3.setGeometry(QtCore.QRect(30, 390, 226, 24))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.widget4 = QtWidgets.QWidget(self.frame)
        self.widget4.setGeometry(QtCore.QRect(310, 290, 240, 61))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget4)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_prediction)

        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_prediction(self):
        veg = self.comboBox.currentText()
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        print('a = ', a)
        print('b = ', b)
        print('Vegitation: ', veg)
        self.lineEdit_3.setText('fire')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose the machine learning algorithm:"))
        self.pushButton_2.setText(_translate("MainWindow", "Train"))
        self.knn_Button.setText(_translate("MainWindow", "KNN"))
        self.SVM_Button.setText(_translate("MainWindow", "SVM"))
        self.NN_Button.setText(_translate("MainWindow", "NN"))
        self.label_3.setText(_translate("MainWindow", "Vegitation"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Brush"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Forest"))
        self.label_4.setText(_translate("MainWindow", "Temp"))
        self.label_5.setText(_translate("MainWindow", "Wind Speed"))
        self.pushButton.setText(_translate("MainWindow", "Predict"))
        self.label_2.setText(_translate("MainWindow", "Prediction result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

