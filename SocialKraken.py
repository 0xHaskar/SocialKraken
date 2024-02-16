import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFrame, QVBoxLayout, QWidget, QPlainTextEdit, QLineEdit
from PyQt5.QtCore import Qt

#окна
#from info import InfoWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SocialKraken")
        self.setGeometry(100, 100, 1000, 550)

        menubar = self.menuBar()

        # Создаем меню
        help_menu = menubar.addMenu("Menu")
        social_menu = menubar.addMenu("Social")
        osint_menu = menubar.addMenu("Osint")
        leaks_menu = menubar.addMenu("Leaks")
        malware_menu = menubar.addMenu("Malware")
        protect_menu = menubar.addMenu("Protect")

        # Создаем подкатегории в Menu
        help_action = QAction("Help", self)
        info_action = QAction("Info", self)
        modules_action = QAction("Modules", self)
        
        # Создаем подкатегории в Social
        beef_xss_action = QAction("beef-xss", self)
        zphisher_action = QAction("zphisher", self)
        
        # Создаем подкатегории в Osint
        snoop_action = QAction("Snoop", self)
        ghunt_action = QAction("Ghunt", self)
        
        # Создаем подкатегории в Malware
        discrod_rat_action = QAction("Malware (Discord-RAT)", self)




        # Назначаем подкатегории в Menu
        help_menu.addAction(help_action)
        help_menu.addAction(info_action)
        help_menu.addAction(modules_action)
        
        # Назначаем подкатегории в Social
        social_menu.addAction(beef_xss_action)
        social_menu.addAction(zphisher_action)
        
        # Назначаем подкатегории в Osint
        osint_menu.addAction(snoop_action)
        osint_menu.addAction(ghunt_action)
        
        # Назначаем подкатегории в Malware
        malware_menu.addAction(discrod_rat_action)




        # Создаем фрейм
        self.frame = QFrame(self)
        self.frame.setGeometry(50, 50, 700, 200)  # Изменен размер поля self.frame

        # Создаем поле информации
        self.information_field = QPlainTextEdit(self)  # Создаем новое поле для вывода информации
        self.information_field.setGeometry(50, 270, 700, 200)  # Изменен размер и положение поля

        # Создаем консоль (поле вывода)
        self.console = QPlainTextEdit(self)
        self.console.setGeometry(50, 500, 700, 200)  # Изменен размер поля self.console

        # Создаем поле для ввода команд
        self.command_input = QLineEdit(self)
        self.command_input.setGeometry(50, 720, 500, 30)  # Изменен положение поля self.command_input

        # Добавляем виджеты в главное окно
        layout = QVBoxLayout()
        layout.addWidget(self.frame)
        layout.addWidget(self.information_field)
        layout.addWidget(self.console)
        layout.addWidget(self.command_input)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)



        # Подключаем обработчик события для запуска скрипта с новым терминалом
        #menu
        info_action.triggered.connect(self.run_menu_info)
        #social
        beef_xss_action.triggered.connect(self.run_beef_xss)
        zphisher_action.triggered.connect(self.run_zphisher)
        #osint
        snoop_action.triggered.connect(self.run_snoop)

        # Подключаем обработчик события для отправки команды
        self.command_input.returnPressed.connect(self.send_command)

    # функции
    def run_beef_xss(self):
        dir = os.getcwd()
        os.chdir(dir + "/Modules/Social/beef-xss/")
        os.system('gnome-terminal -- bash -c "python3 beef.py; exec bash"')
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
    
    def run_zphisher(self):
        dir = os.getcwd()
        os.chdir(dir + "/Modules/Social/zphisher/")
        subprocess.run(['python3', 'zphisher.py'])
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
    
        
    def run_snoop(self):
        dir = os.getcwd()
        os.chdir(dir + "/Modules/Osint/Snoop/")
        #os.system('gnome-terminal -- bash -c "python3 snoop.py; exec bash"')
        subprocess.run(['python3', 'snoop.py'])
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
    
    def run_menu_info(self):
        dir = os.getcwd()
        os.chdir(dir + "/Modules/Menu/")
        subprocess.run(['python3', 'info.py'])
        os.chdir("..")
        os.chdir("..")
        # self.infowindow = InfoWindow(self)
        # self.infowindow.show()

    # консоль команды
    def send_command(self):
        command = self.command_input.text()
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        self.console.appendPlainText(output.decode())
        self.command_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
