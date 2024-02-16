# -*- coding: UTF-8 -*-
import os

os.system('sudo apt-get install openjdk-11-jdk* -y')

os.system('curl -LJO https://github.com/Morsmalleo/AhMyth/releases/download/v1.0-beta.4/AhMyth-Setup_amd64-Linux.deb')

os.system('sudo dpkg -i AhMyth-Setup_amd64-Linux.deb')

print("Запуск:")
os.system('sudo ahmyth --no-sandbox')

