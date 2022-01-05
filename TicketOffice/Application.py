import sys

from PyQt5 import QtWidgets

from ServiceRegistrationWindow import Main
from ServiceAdminWindow import AdminWindow


def application():
    app = QtWidgets.QApplication(sys.argv)
    m = Main()
    # m = AdminWindow()
    m.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()