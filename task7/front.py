from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from utils import dataframe_utils
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 600))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 511, 291))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 40, 511, 291))
        self.label_2.setObjectName("label_2")
        self.label_2.setScaledContents(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 380, 31, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 540, 84, 34))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 460, 31, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 420, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(940, 420, 31, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.dataframe_copy = 0
        self.plt_instanse = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "No image"))
        self.label_2.setText(_translate("MainWindow", "No image"))
        self.pushButton.setText(_translate("MainWindow", "^"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton_3.setText(_translate("MainWindow", "v"))
        self.pushButton_4.setText(_translate("MainWindow", "<"))
        self.pushButton_5.setText(_translate("MainWindow", ">"))

    def add_functions(self):
        self.pushButton_2.clicked.connect(lambda: self.open_f())
        self.pushButton.clicked.connect(lambda: self.up())
        self.pushButton_3.clicked.connect(lambda: self.down())
        self.pushButton_4.clicked.connect(lambda: self.left())
        self.pushButton_5.clicked.connect(lambda: self.right())
    
    def open_f(self):
        file_name = QFileDialog.getOpenFileName(self.centralwidget)[0]

        dataframe = dataframe_utils.get_dataframe_from_file(file_name, skip_before=2)
        dataframe.rename(
            columns={0: 'Energy', 1: '<xanes>'},
            inplace=True
        )

        self.dataframe_copy = dataframe

        plt.plot(dataframe['Energy'], dataframe['<xanes>'])
        plt.savefig('im_orig.png')
        self.label.setPixmap(QtGui.QPixmap('im_orig.png'))

        self.plt_instanse = plt.plot(self.dataframe_copy['Energy'], self.dataframe_copy['<xanes>'], color="red")
        plt.savefig('im_copy.png')
        self.label_2.setPixmap(QtGui.QPixmap('im_copy.png'))

    def up(self):
        plt.clf()
        self.dataframe_copy['<xanes>'] += 1
        self.plt_instanse =plt.plot(self.dataframe_copy['Energy'], self.dataframe_copy['<xanes>'], color="red")
        plt.savefig('im_copy.png')
        self.label_2.setPixmap(QtGui.QPixmap('im_copy.png'))

    def down(self):
        plt.clf()
        self.dataframe_copy['<xanes>'] -= 1
        self.plt_instanse =plt.plot(self.dataframe_copy['Energy'], self.dataframe_copy['<xanes>'], color="red")
        plt.savefig('im_copy.png')
        self.label_2.setPixmap(QtGui.QPixmap('im_copy.png'))

    def right(self):
        plt.clf()
        self.dataframe_copy['Energy'] += 1
        self.plt_instanse =plt.plot(self.dataframe_copy['Energy'], self.dataframe_copy['<xanes>'], color="red")
        plt.savefig('im_copy.png')
        self.label_2.setPixmap(QtGui.QPixmap('im_copy.png'))

    def left(self):
        plt.clf()
        self.dataframe_copy['Energy'] -= 1
        self.plt_instanse =plt.plot(self.dataframe_copy['Energy'], self.dataframe_copy['<xanes>'], color="red")
        plt.savefig('im_copy.png')
        self.label_2.setPixmap(QtGui.QPixmap('im_copy.png'))

    