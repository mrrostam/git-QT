import sys

from PyQt5 import QtWidgets, QtGui

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QWidget()
    main_window.show()
    sys.exit(app.exec_())