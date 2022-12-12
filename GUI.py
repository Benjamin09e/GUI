from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PySide6.QtGui import QIcon, QFont
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)

app = QApplication()

window = MainWindow()

#app = QApplication()
appIcon = QIcon("downloads.png")

#window = QWidget()

window.setWindowTitle("Frist GUI")
window.setWindowIcon(appIcon)
window.setFixedSize(500, 300)

#buttons
btnAccept = QPushButton("Accepte", parent=window)
btn_font = QFont("Poppins", 12)
btnAccept.setFont(btn_font)
btnAccept.move(180, 230)
btnAccept.setStyleSheet("QPushButton {background-color: #2d3e4e; color: white}")

btnClosed = QPushButton("Closed", parent=window)
btn_font = QFont("Poppins", 12)
btnClosed.setFont(btn_font)
btnClosed.move(270, 230)
btnClosed.setStyleSheet("QPushButton {background-color: white; color:#2d3e4e }")


window.show()
app.exec()