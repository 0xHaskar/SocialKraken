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

os.system('wget https://github.com/snooppr/snoop/releases/download/v1.4.1__2024_6_13/Snoop_for_GNU_Linux.rar')

os.system('unrar e Snoop_for_GNU_Linux.rar')

os.system('chmod +x snoop_cli')

print(colr.RED + colr.BOLD + "Не забудь прочитать руководство! Оно находится в /modules/snoop/" + colr.END)