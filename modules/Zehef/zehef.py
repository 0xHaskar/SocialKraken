# -*- coding: UTF-8 -*-
import os

os.system('git clone https://github.com/N0rz3/Zehef.git')

dir = os.getcwd()
os.chdir(dir + "/Zehef")

os.system('pip3 install -r requirements.txt')
