import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QScrollArea
from PyQt5.QtGui import QPixmap

class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание окна
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle("Информация о ShadowStrike")

        # Создание основного виджета
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Создание компоновщика QVBoxLayout
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Добавление логотипа PNG
        logo_label = QLabel(self)
        logo_pixmap = QPixmap("logo.png")
        logo_label.setPixmap(logo_pixmap)
        layout.addWidget(logo_label)

        # Создание виджета QScrollArea
        scroll_area = QScrollArea(self)
        layout.addWidget(scroll_area)

        # Создание виджета QLabel для лицензии
        license_label = QLabel(self)
        with open("license.txt", "r") as file:
            license_text = file.read()
        license_label.setText(license_text)

        # Установка лицензии в виджет QScrollArea
        scroll_area.setWidget(license_label)

        # Добавление текста "by 0xHaskar"
        text_label = QLabel(self)
        text_label.setText("by 0xHaskar")
        layout.addWidget(text_label)

        # Добавление ссылки на Discord
        discord_button = QPushButton(self)
        discord_button.setText("Discord")
        layout.addWidget(discord_button)
        discord_button.clicked.connect(self.open_discord)

        # Добавление ссылки на пожертвование
        donate_button = QPushButton(self)
        donate_button.setText("Donate")
        layout.addWidget(donate_button)
        donate_button.clicked.connect(self.open_donate)

        # Добавление кнопки "Закрыть"
        close_button = QPushButton(self)
        close_button.setText("Закрыть")
        layout.addWidget(close_button)
        close_button.clicked.connect(self.close)

    def open_discord(self):
        webbrowser.open("https://discord.com/invite/Eg8aDS7Hn7")

    def open_donate(self):
        webbrowser.open("https://www.donationalerts.com/r/xackapb")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfoWindow()
    window.show()
    sys.exit(app.exec_())
