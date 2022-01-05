import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog


class Ui_Dialog(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("Dialog")
        AdminWindow.resize(640, 450)
        AdminWindow.setSizeGripEnabled(False)

        font_label = QtGui.QFont()
        font_label.setFamily("italic")
        font_label_size = 10
        font_label.setPointSize(font_label_size)

        font_box = QtGui.QFont()
        font_box.setFamily("Arial")
        font_box.setPointSize(12)

        self.label_nameFilm = QtWidgets.QLabel(AdminWindow)
        self.label_nameFilm.setGeometry(QtCore.QRect(110, 5, 280, font_label_size * 2))
        self.label_nameFilm.setFont(font_label)

        self.box_nameFilm = QtWidgets.QLineEdit(AdminWindow)
        self.box_nameFilm.setGeometry(QtCore.QRect(110, 30, 420, 31))
        self.box_nameFilm.setFont(font_box)
        self.box_nameFilm.setPlaceholderText("name film")
        self.box_nameFilm.setObjectName("box_nameFilm")

        self.label_dataFilm = QtWidgets.QLabel(AdminWindow)
        self.label_dataFilm.setGeometry(QtCore.QRect(110, 65, 280, font_label_size * 2))
        self.label_dataFilm.setFont(font_label)

        self.box_dataFilm = QtWidgets.QLineEdit(AdminWindow)
        self.box_dataFilm.setGeometry(QtCore.QRect(110, 90, 420, 31))
        self.box_dataFilm.setFont(font_box)
        self.box_dataFilm.setPlaceholderText(str(time.strftime("%d.%m.%Y", time.localtime())))
        self.box_dataFilm.setObjectName("box_dataFilm")

        self.label_timeFilm = QtWidgets.QLabel(AdminWindow)
        self.label_timeFilm.setGeometry(QtCore.QRect(110, 125, 280, font_label_size * 2))
        self.label_timeFilm.setFont(font_label)

        self.box_timeFilm = QtWidgets.QLineEdit(AdminWindow)
        self.box_timeFilm.setGeometry(QtCore.QRect(110, 150, 420, 31))
        self.box_timeFilm.setFont(font_box)
        self.box_timeFilm.setPlaceholderText("12:00")
        self.box_timeFilm.setObjectName("box_timeFilm")

        self.label_hallFilm = QtWidgets.QLabel(AdminWindow)
        self.label_hallFilm.setGeometry(QtCore.QRect(110, 185, 210, font_label_size * 2))
        self.label_hallFilm.setFont(font_label)

        self.box_hallFilm = QtWidgets.QLineEdit(AdminWindow)
        self.box_hallFilm.setGeometry(QtCore.QRect(110, 210, 210, 31))
        self.box_hallFilm.setFont(font_box)
        self.box_hallFilm.setPlaceholderText("1..5")
        self.box_hallFilm.setObjectName("box_hallFilm")

        self.label_durationFilm = QtWidgets.QLabel(AdminWindow)
        self.label_durationFilm.setGeometry(QtCore.QRect(308, 185, 208, font_label_size * 2))
        self.label_durationFilm.setFont(font_label)

        self.box_durationFilm = QtWidgets.QLineEdit(AdminWindow)  # Продолжительность (длительность) фильма
        self.box_durationFilm.setGeometry(QtCore.QRect(308, 210, 210, 31))
        self.box_durationFilm.setFont(font_box)
        self.box_durationFilm.setPlaceholderText("1:30")
        self.box_durationFilm.setObjectName("box_durationFilm")

        self.label_priceArmchairFilm = QtWidgets.QLabel(AdminWindow)
        self.label_priceArmchairFilm.setGeometry(QtCore.QRect(110, 245, 210, font_label_size * 2))
        self.label_priceArmchairFilm.setFont(font_label)

        self.box_priceArmchairFilm = QtWidgets.QLineEdit(AdminWindow)
        self.box_priceArmchairFilm.setGeometry(QtCore.QRect(110, 270, 208, 31))
        self.box_priceArmchairFilm.setFont(font_box)
        self.box_priceArmchairFilm.setPlaceholderText("200")
        self.box_priceArmchairFilm.setObjectName("box_priceArmchairFilm")

        self.label_priceSofaFilm = QtWidgets.QLabel(AdminWindow)
        self.label_priceSofaFilm.setGeometry(QtCore.QRect(308, 245, 210, font_label_size * 2))
        self.label_priceSofaFilm.setFont(font_label)

        self.box_priceSofaFilm = QtWidgets.QLineEdit(AdminWindow)
        self.box_priceSofaFilm.setGeometry(QtCore.QRect(308, 270, 210, 31))
        self.box_priceSofaFilm.setFont(font_box)
        self.box_priceSofaFilm.setPlaceholderText("400")
        self.box_priceSofaFilm.setObjectName("box_priceSofaFilm")

        btn_w = 140
        btn_h = 30
        btn_resize_w = 60
        btn_resize_h = 370
        btn_space = 40

        self.btn = QtWidgets.QPushButton(AdminWindow)
        self.btn.setGeometry(QtCore.QRect(btn_resize_w, btn_resize_h, btn_w, btn_h))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn.setFont(font)
        self.btn.setObjectName("sign_in")

        self.btn1 = QtWidgets.QPushButton(AdminWindow)
        self.btn1.setGeometry(QtCore.QRect(btn_resize_w + btn_w + btn_space, btn_resize_h, btn_w, btn_h))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn1.setFont(font)
        self.btn1.setObjectName("sign_in")

        self.btn2 = QtWidgets.QPushButton(AdminWindow)
        self.btn2.setGeometry(QtCore.QRect(btn_resize_w + (btn_w + btn_space) * 2, btn_resize_h, btn_w, btn_h))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn2.setFont(font)
        self.btn2.setObjectName("sign_in")

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("Dialog", "Admin"))
        self.label_nameFilm.setText(_translate("Dialog", "Название фильма"))
        self.label_dataFilm.setText(_translate("Dialog", "Дата фильма (дд.мм.гггг)"))
        self.label_timeFilm.setText(_translate("Dialog", "время фильма (чч:мм)"))
        self.label_hallFilm.setText(_translate("Dialog", "Номер кинозала"))
        self.label_durationFilm.setText(_translate("Dialog", "Длительность фильма"))
        self.label_priceArmchairFilm.setText(_translate("Dialog", "Цена на кресло"))
        self.label_priceSofaFilm.setText(_translate("Dialog", "Цена на диван"))


class AdminWindow(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.setupUi(self)
