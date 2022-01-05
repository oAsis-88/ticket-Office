import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLineEdit, QDialog, QWidget, QMainWindow

from ServiceUserWindow import UserWindow
from ServiceAdminWindow import AdminWindow


class Ui_Dialog(object):
    def setupUi(self, Main):
        Main.setObjectName("Dialog")
        Main.resize(439, 239)
        Main.setFixedSize(439, 239)
        # Main.setSizeGripEnabled(False)

        self.box_username = QtWidgets.QLineEdit(Main)
        self.box_username.setGeometry(QtCore.QRect(10, 30, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.box_username.setFont(font)
        self.box_username.setPlaceholderText("username")
        self.box_username.setObjectName("box_username")

        self.box_password = QtWidgets.QLineEdit(Main)
        self.box_password.setEchoMode(QLineEdit.Password)
        self.box_password.setGeometry(QtCore.QRect(10, 70, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.box_password.setFont(font)
        self.box_password.setPlaceholderText("Password")
        self.box_password.setObjectName("box_password")

        self.error_inputs = QtWidgets.QLabel(Main)
        self.error_inputs.setGeometry(QtCore.QRect(80, 130, 280, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.error_inputs.setFont(font)
        pal = self.error_inputs.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.error_inputs.setPalette(pal)
        self.error_inputs.setObjectName("error_inputs")

        self.password_display = QtWidgets.QCheckBox(Main)
        self.password_display.setGeometry(QtCore.QRect(15, 101, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.password_display.setFont(font)
        self.password_display.setObjectName("password_display")

        self.password_display_label = QtWidgets.QLabel(Main)
        self.password_display_label.setGeometry(QtCore.QRect(35, 100, 280, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.password_display_label.setFont(font)
        self.password_display_label.setObjectName("password_display_label")

        self.sign_in = QtWidgets.QPushButton(Main)
        self.sign_in.setGeometry(QtCore.QRect(162, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.sign_in.setFont(font)
        self.sign_in.setObjectName("sign_in")
        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Dialog", "Log in to your account"))
        self.password_display_label.setText(_translate("Dialog", "- display password"))
        self.sign_in.setText(_translate("Dialog", "Sign in"))


class Main(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.sign_in.clicked.connect(self.sign_in_clicked)
        self.password_display.stateChanged.connect(self.changeTitle)

    @QtCore.pyqtSlot()
    def sign_in_clicked(self):
        username_input = self.box_username.text()
        password_input = self.box_password.text()
        if not username_input or not password_input:
            self.error_inputs.setText("Incorrect username or password.")
        if username_input == "123" or password_input == "123":
            self.hide()

            self.ui = UserWindow()
            self.ui.exec()

            self.show()
        elif username_input == "1234" or password_input == "1234":
            self.hide()

            self.ui = AdminWindow()
            self.ui.exec()

            self.show()
        else:
            self.error_inputs.setText("Incorrect username or password.")

    def changeTitle(self):
        if self.password_display.isChecked():
            self.box_password.setEchoMode(QLineEdit.Normal)
        else:
            self.box_password.setEchoMode(QLineEdit.Password)




