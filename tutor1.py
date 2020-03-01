import sys

from PyQt5 import QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('Tutor1 - OOP')
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MyWindow()
    sys.exit(app.exec_())