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

#emoji
#print(u'\U0001F441') eye
#print(u'\U0001FA78') blood
#print(u'\U0001F3C1') finish

#os.system('gnome-terminal -e "bash -c nmap;bash"')

print(colr.GREEN + colr.BOLD + '''
殪幢緻Iii爰曷樔黎㌢´　　｀ⅷ
艇艀裲f睚鳫巓襴骸　　　　贒憊
殪幢緻I翰儂樔黎夢'”　 　 ,ｨ傾
盥皋袍i耘蚌紕偸′　　　 雫寬I
悗f篝嚠篩i縒縡齢　　 　 Ⅷ辨f
輯駲f迯瓲i軌帶′　　　　　守I厖孩
Developed by 0xHaskar
''')
#print(colr.BLUE + colr.BOLD + '1. First Blood'+ u'\U0001FA78')
print('''
      Программное обеспечение представлено исключительно
      в информационных целях и предназначено только для ознакомления! 
      Скачивая программу, вы соглашаетесь с тем,
      что все действия находятся на вашей ответственности и совести! 
      Вы согласны со всем, что написано на этой странице!
      ''')

select = input('Принять? Да/Нет: ')

if (select == 'Да') or (select == 'да') or (select == 'lf'):
   os.system("clear")
   
   print(colr.GREEN + colr.BOLD + '''
殪幢緻Iii爰曷樔黎㌢´　　｀ⅷ
艇艀裲f睚鳫巓襴骸　　　　贒憊
殪幢緻I翰儂樔黎夢'”　 　 ,ｨ傾
盥皋袍i耘蚌紕偸′　　　 雫寬I
悗f篝嚠篩i縒縡齢　　 　 Ⅷ辨f
輯駲f迯瓲i軌帶′　　　　　守I厖孩

SocialKraken 1.0 Beta
Developed by 0xHaskar
''')
   
   print('Напиши help')
   while True:
      select = input(colr.BLUE + colr.BOLD + "> ")
      if select == "help":
         print(colr.END + colr.CYAN + '''
            AhMyth - android RAT:
               ahmyth 
               ahmyth install
               
            BigBro - geolocation:
               bigbro 
               bigbro install
               После установки Откройте api.py и впишите туда токен ngrok
               
            HiddenEye - fishing:
               hiddeneye
               hiddeneye install
               
            Maltego:
               maltego
        ''')

      elif select == "ahmyth":
         print('\U0001F985' + colr.END + colr.CYAN + ' AhMyth start')
         os.system('gnome-terminal -- bash -c "sudo ahmyth --no-sandbox; exec bash"')
         
      elif select == "ahmyth install":
         print('\U0001F985' + colr.END + colr.CYAN + ' AhMyth install:')
         dir = os.getcwd()
         os.chdir(dir + "/modules/AhMyth/")
         os.system("python3 ahmyth.py")
         
      elif select == "bigbro":
         print(colr.END + colr.CYAN + ' BigBro start:')
         dir = os.getcwd()
         os.chdir(dir + "/modules/BigBro/Bigbro")
         os.system("python3 start.py")
         
         
      elif select == "bigbro install":
         print(colr.END + colr.CYAN + ' BigBro install:')
         dir = os.getcwd()
         os.chdir(dir + "/modules/BigBro/")
         os.system("python3 bigbro.py")


      elif select == "hiddeneye":
         print(colr.END + colr.CYAN + ' HiddenEye install:')
         dir = os.getcwd()
         os.chdir(dir + "/modules/HiddenEye/HiddenEye")
         os.system("python3 HiddenEye.py")
      
      elif select == "hiddeneye install":
               print(colr.END + colr.CYAN + ' HiddenEye install:')
               dir = os.getcwd()
               os.chdir(dir + "/modules/HiddenEye/")
               os.system("python3 hiddeneye.py")
      
      
      elif select == "maltego":
         print(colr.END + colr.CYAN + '\U0001F441' + ' Maltego start:')
         os.system('gnome-terminal -- bash -c "maltego; exec bash"')
         
      
   
elif (select == 'Нет') or (select == 'нет'): 
   print(colr.BLUE + colr.BOLD + 'Пока ^-^')