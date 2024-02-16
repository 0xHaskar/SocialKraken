import sys
import base64
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
import subprocess

class LicenseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SocialKraken")
        self.setGeometry(100, 100, 500, 300)  # Установите желаемые размеры окна

        # Логотип в правом верхнем углу
        logo_label = QLabel(self)
        pixmap = QPixmap("logo.png")  # Замените "path_to_logo.png" на путь к вашему логотипу
        logo_label.setPixmap(pixmap)
        logo_label.setGeometry(130, 10, 1000, 100)  # Установите желаемые координаты и размеры логотипа

        # Поле с лицензией
        license_text_edit = QTextEdit(self)
        license_text_edit.setGeometry(50, 100, 400, 100)  # Установите желаемые координаты и размеры поля с лицензией
        with open("license.txt", "r") as file:  # Замените "path_to_license.txt" на путь к вашему файлу с лицензией
            license_text = file.read()
            license_text_edit.setPlainText(license_text)
        license_text_edit.setReadOnly(True)

        # Поле для ввода ключа
        key_label = QLabel(self)
        key_label.setText("Key:")
        key_label.setGeometry(50, 220, 50, 20)  # Установите желаемые координаты и размеры метки "Key:"
        key_input = QLineEdit(self)
        key_input.setGeometry(100, 220, 200, 20)  # Установите желаемые координаты и размеры поля для ввода ключа
        key_input.setEchoMode(QLineEdit.Password)

        # Кнопка "принять"
        accept_button = QPushButton(self)
        accept_button.setText("Принять")
        accept_button.setGeometry(350, 250, 100, 30)  # Установите желаемые координаты и размеры кнопки "принять"
        accept_button.clicked.connect(self.check_key)

    def check_key(self):
        key_input = self.findChild(QLineEdit).text()
        key = key_input
        encoded_key = base64.b64encode(key.encode()).decode()
        if encoded_key == "U1M=":
            subprocess.Popen(["python3", "SocialKraken.py"])
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Неверный ключ или пароль")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LicenseWindow()
    window.show()
    sys.exit(app.exec_())
