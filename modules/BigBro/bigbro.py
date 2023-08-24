# -*- coding: UTF-8 -*-
import os

os.system('git clone https://github.com/Bafomet666/Bigbro')

dir = os.getcwd()
os.chdir(dir + "/Bigbro")

os.system('pip3 install -r requerements.txt')

print("=============================")
print("Откройте api.py и впишите туда токен ngrok")


