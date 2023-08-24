# -*- coding: UTF-8 -*-

import os

class colr:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
os.system('git clone https://github.com/lamer112311/Dnnme2')

dir = os.getcwd()
os.chdir(dir + "/Dnnme2/")

os.system('pip3 install -r requirements.txt')

#os.system('python build.py')
   
print(colr.RED + colr.BOLD + "Не забудь прочитать гайд!" + colr.END)
print(colr.RED + colr.BOLD + "https://telegra.ph/Sozdaem-bota-dlya-deanonimizacii-04-26" + colr.END)
