# -*- coding: UTF-8 -*-
import os

os.system('git clone https://github.com/Bafomet666/OSINT-SAN.git')

dir = os.getcwd()
os.chdir(dir + "/OSINT-SAN")

os.system('pip3 install -r requirements.txt')

print("=============================")
print("Обратитесь за помощью: https://github.com/Bafomet666/OSINT-SAN")