import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QToolTip
from PyQt5 import QtCore

class SnoopWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ghunt')

        # Поле для email с подсказкой
        self.email_label = QLabel('Email(Gmail):')
        self.email_input = QLineEdit()
        self.email_input.setToolTip('Введите вашу почту Gmail')  # Добавление подсказки

        # Выпадающий список параметров
        self.param_label = QLabel('Параметр:')
        self.param_combo = QComboBox()
        self.param_combo.addItem('Параметр 1')
        self.param_combo.addItem('Параметр 2')
        self.param_combo.addItem('Параметр 3')

        # Кнопка поиска
        self.search_button = QPushButton('Поиск')
        self.search_button.clicked.connect(self.search)

        # Создание вертикального макета и добавление элементов
        layout = QVBoxLayout()
        layout.setSpacing(10)  # Установка расстояния между виджетами
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.param_label)
        layout.addWidget(self.param_combo)
        layout.addWidget(self.search_button)

        # Выравнивание меток справа
        self.email_label.setAlignment(QtCore.Qt.AlignRight)
        self.param_label.setAlignment(QtCore.Qt.AlignRight)

        self.setLayout(layout)
        self.resize(400, 200)  # Изменение размеров окна
        self.center()  # Вызов функции для выравнивания окна по центру

        self.show()

    def center(self):
        # Функция для выравнивания окна по центру экрана
        frame_geometry = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def search(self):
        email = self.email_input.text()
        param = self.param_combo.currentText()
        os.system('sudo chmod +x ghunt_cli')
        os.system('gnome-terminal -- bash -c "./ghunt_cli '+ email +'; exec bash"')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    snoop_window = SnoopWindow()
    sys.exit(app.exec_())
