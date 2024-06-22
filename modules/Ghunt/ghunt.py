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

os.system('pip3 install ghunt')

print(colr.RED + colr.BOLD + "Установлено! Проверьте ошибки!" + colr.END)
print(colr.BLUE + colr.BOLD + "https://github.com/mxrch/GHunt" + colr.END)

print(colr.BLUE + colr.BOLD + ''' 
Usage: ghunt [-h] {login,email,gaia,drive,geolocate} ...

Positional Arguments:
  {login,email,gaia,drive,geolocate}
    login               Authenticate GHunt to Google.
    email               Get information on an email address.
    gaia                Get information on a Gaia ID.
    drive               Get information on a Drive file or folder.
    geolocate           Geolocate a BSSID.

Options:
  -h, --help            show this help message and exit
''' + colr.END)

print(colr.RED + colr.BOLD + "Ghunt установлен в систему!" + colr.END)
#export PATH="$PATH:/home/kali/.local/bin"

print(colr.BLUE + colr.BOLD + '''
Если не прошел PATCH,то используйте:
export PATH="$PATH:/home/kali/.local/bin" 
kali - имя пользователя!
''' + colr.END)
