import sys
from PyQt5.Qt import QIcon, QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton


class ChrysalisFM(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setCentralWidget(FMWidget())
        self.setWindowTitle("Chrysalis")
        self.show()


class FMWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.view = ColumnView()

        self.buttonBack = QPushButton()
        self.buttonForward = QPushButton()
        self.buttonUp = QPushButton()
        self.buttonReload = QPushButton()

        self.initUI()

    def initUI(self):
        self.layout.addWidget(self.buttonBack, 0, 0)
        self.buttonBack.setIcon(QIcon.fromTheme("go-previous"))
        self.buttonBack.setIconSize(QSize(32, 32))
        self.layout.addWidget(self.buttonForward, 0, 1)
        self.buttonForward.setIcon(QIcon.fromTheme("go-next"))
        self.buttonForward.setIconSize(QSize(32, 32))
        self.layout.addWidget(self.buttonUp, 0, 2)
        self.buttonUp.setIcon(QIcon.fromTheme("go-up"))
        self.buttonUp.setIconSize(QSize(32, 32))

        self.setLayout(self.layout)


class ColumnView(QWidget):
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fm = ChrysalisFM()
    sys.exit(app.exec_())
