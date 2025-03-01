# -*- coding: UTF-8 -*-
import os
import base64


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

# Пароль, закодированный в base64
encoded_password = 'U0s='

def check_password(password):
    if base64.b64decode(encoded_password.encode()).decode() == password:
        return True
    else:
        return False

print(colr.GREEN + colr.BOLD + '''
殪幢緻Iii爰曷樔黎㌢´　　｀ⅷ
艇艀裲f睚鳫巓襴骸　　　　贒憊
殪幢緻I翰儂樔黎夢'"　 　 ,ｨ傾
盥皋袍i耘蚌紕偸′　　　 雫寬I
悗f篝嚠篩i縒縡齢　　 　 Ⅷ辨f
輯駲f迯瓲i軌帶′　　　　　守I厖孩
Developed by 0xHaskar
''')

password = input('Введите пароль: ')

if check_password(password):
   os.system("clear")
   os.system("python3 SocialKraken.py")
else:
    print(colr.RED + 'Неверный пароль!' + colr.END)
