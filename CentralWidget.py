import PyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QTextBrowser, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import pyqtSlot, Qt, QSize


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout(self)

        self.user = QLineEdit(parent)

        self.password = QLineEdit(parent)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.button = QPushButton(parent)
        self.button.setText("Login")
        self.button.clicked.connect(self.check_password)

        layout.addWidget(QLabel("Benutername:"), 1, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Kennwort:"), 2, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.user, 1, 2)
        layout.addWidget(self.password, 2, 2)
        layout.addWidget(self.button, 3, 1, 1, 2)

        self.setLayout(layout)

        # Erweiterung: Platzhalter "Max Mustermann"
        self.user.setPlaceholderText("Max Mustermann")

        # Erweiterung:
        # - Aus Grossbuchstaben werden mittels < Kleinbuchstaben
        # - Eingabe von mindestens einem und hochstens sechs Buchstaben
        # - Anzahl der Buchstaben wird mit _ dargestellt.
        self.user.setInputMask("<Aaaaaa;_")

        # Erweiterung: Icon fuer das Button
        self.button.setIcon(QIcon("./shark.png"))
        self.button.setIconSize(QSize(100, 100))

    @pyqtSlot()
    def check_password(self):
        print("clicked")

        if self.password.text() == "abc123" and self.user.text() == "Herr Hey":
            print("success")