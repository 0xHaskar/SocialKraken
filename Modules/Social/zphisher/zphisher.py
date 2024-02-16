import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import subprocess

class ZphisherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ZPhisher')
        self.setGeometry(100, 100, 300, 200)

        install_button = QPushButton('Install', self)
        start_button = QPushButton('Start', self)

        layout = QVBoxLayout()
        layout.addWidget(install_button)
        layout.addWidget(start_button)

        self.setLayout(layout)

        install_button.clicked.connect(self.install_clicked)
        start_button.clicked.connect(self.start_clicked)

    def install_clicked(self):
        os.system('gnome-terminal -- bash -c "git clone --depth=1 https://github.com/htr-tech/zphisher.git; exec bash"')
        # os.system('cd zphisher')
        # os.system('bash zphisher.sh')


    def start_clicked(self):
        dir = os.getcwd()
        os.chdir(dir + "/zphisher/")
        os.system('gnome-terminal -- bash -c "bash zphisher.sh; exec bash"')
        os.chdir("..")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ZphisherWindow()
    window.show()
    sys.exit(app.exec_())
