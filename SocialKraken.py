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
print(colr.RED + '''
         +----------------------------------------------------------------+          
   (__)  |Программное обеспечение представлено исключительно              |
(|)(00)  |в информационных целях и предназначено только для ознакомления! | 
 |/(__)\ |Используя программу, вы соглашаетесь с тем,                     |
 |_/ _|  |что все действия находятся на вашей ответственности и совести!  | 
         |Автор не несет ответственность за ваши действия!                |
         |Вы согласны со всем, что написано на этой странице!             |
         +----------------------------------------------------------------+
      ''')

select = input(colr.GREEN + colr.BOLD + 'Принять? yes/not: ')

if (select == 'Да') or (select == 'да') or (select == 'lf') or (select == 'yes') or (select == 'Yes'):
   os.system("clear")
   
   print(colr.GREEN + colr.BOLD + '''
殪幢緻Iii爰曷樔黎㌢´　　｀ⅷ
艇艀裲f睚鳫巓襴骸　　　　贒憊
殪幢緻I翰儂樔黎夢'”　 　 ,ｨ傾
盥皋袍i耘蚌紕偸′　　　 雫寬I
悗f篝嚠篩i縒縡齢　　 　 Ⅷ辨f
輯駲f迯瓲i軌帶′　　　　　守I厖孩

SocialKraken b2.0 (Remake):
Developed by 0xHaskar [https://github.com/0xHaskar/]
''')
   
   
   print(colr.END + colr.RED + 'Напиши help')
   while True:
      #select = input(colr.BLUE + colr.BOLD + '\U0001F419' + "> ")
      select = input(colr.BLUE + colr.BOLD + 'SocialKreaken ' + "> ")
      if select == "help":
         print(colr.END + colr.CYAN + '''

            Ghunt - Поиск информации Gmail
                  ghunt -- запуск
                  ghunt install -- установка 
            #https://github.com/mxrch/GHunt
         
            OSINT-SAN - Бесплатный и общедоступный OSINT SAN Framework
               osint-san -- запуск
               osint-san install -- установка 
            #https://github.com/Bafomet666/OSINT-SAN
            
            BigBro - geolocation:
               bigbro 
               bigbro install
               После установки Откройте api.py и впишите туда токен ngrok
               
            HiddenEye - fishing:
               hiddeneye
               hiddeneye install
               
            Snoop - инструмент разведки на основе открытых данных по нику
               snoop
               snoop install
               # https://github.com/snooppr/snoop
               
            Dnnme2 - фейк бот ТГ
               dnnme2
               dnnme2 install
               # гайд -> https://telegra.ph/Sozdaem-bota-dlya-deanonimizacii-04-26
               
            Zehef - для отслеживания электронной почты (Нестабильный, ошибки)
               zehef
               zehef install
               
            Sherlock:
               sherlock
               sherlock install
               
            Maltego:
               maltego - запуск
               maltego install - установка
               
         Exploits:
            В разработке!
      ''')
       
      # Ghunt
      elif select == "ghunt install" or select == "Ghunt install":
         print (colr.END + colr.GREEN + ' Ghunt install' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Ghunt/")
         os.system('gnome-terminal -- bash -c "python3 ghunt.py; exec bash"')
         os.chdir("..")
         os.chdir("..")     


      # OSINT-SAN
      elif select == "osint-san" or select == "san":
         print (colr.END + colr.GREEN + ' OSINT-SAN start' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/OSINT-SAN/OSINT-SAN/")
         os.system('gnome-terminal -- bash -c "python3 osintsan.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         os.chdir("..")

      elif select == "osint-san install" or select == "san install":
         print (colr.END + colr.GREEN + ' OSINT-SAN install' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/OSINT-SAN/")
         os.system('gnome-terminal -- bash -c "python3 osintsan.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         
      # BigBro   
      elif select == "bigbro":
         print(colr.END + colr.GREEN + ' BigBro start:' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/BigBro/Bigbro")
         os.system("python3 start.py")
         
         
      elif select == "bigbro install":
         print(colr.END + colr.GREEN + ' BigBro install:' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/BigBro/")
         os.system("python3 bigbro.py")

      # HiddenEye
      elif select == "hiddeneye":
         print(colr.END + colr.GREEN + ' HiddenEye start:' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/HiddenEye/HiddenEye")
         os.system("python3 HiddenEye.py")
      
      elif select == "hiddeneye install":
               print(colr.END + colr.GREEN + ' HiddenEye install:'+ colr.CYAN)
               dir = os.getcwd()
               os.chdir(dir + "/modules/HiddenEye/")
               os.system("python3 hiddeneye.py")
      # snoop    
      elif select == "snoop":
         print (colr.END + colr.GREEN + ' start snoop' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Snoop/")
         user = input("Username: ")
         os.system('gnome-terminal -- bash -c "./snoop_cli ' + user +'; exec bash"')
         os.chdir("..")
         os.chdir("..")
         
      elif select == "snoop install":
         print(colr.END + colr.GREEN + " install snoop github" + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Snoop/")
         os.system('gnome-terminal -- bash -c "python3 snoop.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         
      # Dnnme2
      elif select == "dnnme2":
         print(colr.END + colr.GREEN + " Dnnme2 start " + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Dnnme2/Dnnme2")
         os.system('gnome-terminal -- bash -c "python3 build.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         os.chdir("..")
      
      elif select == "dnnme2 install":
         print(colr.END + colr.GREEN + " Dnnme2 install" + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Dnnme2/")
         os.system('gnome-terminal -- bash -c "python3 dnnme2.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         
      # Zehef
      elif select == "zehef":
         print(colr.END + colr.GREEN + " Zehef start " + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Zehef/Zehef")
         os.system('gnome-terminal -- bash -c "python3 zehef.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         os.chdir("..")
      
      elif select == "zehef install":
         print(colr.END + colr.GREEN + " Zehef install" + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Zehef/")
         os.system('gnome-terminal -- bash -c "python3 zehef.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         
      # Maltego
      elif select == "maltego":
         print(colr.END + colr.GREEN + '\U0001F441' + ' Maltego start:' + colr.CYAN)
         os.system('gnome-terminal -- bash -c "maltego; exec bash"')
      
      elif select == "maltego install":
            print(colr.END + colr.GREEN + '\U0001F441' + ' Maltego install:' + colr.CYAN)
            os.system('gnome-terminal -- bash -c "sudo apt install maltego; exec bash"')
            
      # Sherlock
      elif select == "sherlock":
         print(colr.END + colr.GREEN + 'Sherlock start:' + colr.CYAN)
         os.system('gnome-terminal -- bash -c "sherlock; exec bash"')
      
      elif select == "sherlock install":
         print(colr.END + colr.GREEN + 'Sherlock install:' + colr.CYAN)
         os.system('gnome-terminal -- bash -c "sudo apt install sherlock; exec bash"')
            
      
   
elif (select == 'Нет') or (select == 'нет') or (select == 'no') or (select == 'not') or (select == 'Not'): 
   print(colr.BLUE + colr.BOLD + 'Пока ^-^')
   
else: 
   print(colr.BLUE + colr.BOLD + 'Пока ^-^')