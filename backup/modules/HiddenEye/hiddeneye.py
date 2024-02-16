# -*- coding: UTF-8 -*-
import os


os.system('git clone https://github.com/Morsmalleo/HiddenEye.git')

os.system('sudo apt install python3-pip') 

dir = os.getcwd()
os.chdir(dir + "/HiddenEye")

os.system('sudo pip3 install -r requirements.txt')

os.system('sudo pip3 install requests')

os.system('sudo chmod 777 HiddenEye.py ')

os.system('python3 HiddenEye.py')

