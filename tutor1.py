import sys

from PyQt5 import QtWidgets, QtGui


class StartNewGameBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("Start New Game")
        self.move(20, 160)


class QuitBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("Quit")
        self.move(150, 160)
        self.clicked.connect(QtWidgets.qApp.quit)
        self.setToolTip("exit!")

class QuitMessage(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText("Do you really want to quit?")
        self.addButton(self.No)
        self.addButton(self.Yes)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('Tutor1.2')
        self.setToolTip("MainWindow.Tooltip")
        self.new_button = StartNewGameBtn(self)
        self.quit_button = QuitBtn(self)
        self.show()

    def closeEvent(self, event):
        reply = QuitMessage().exec_()
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MyWindow()
    sys.exit(app.exec_())
