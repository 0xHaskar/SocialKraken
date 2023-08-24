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
      Используя программу, вы соглашаетесь с тем,
      что все действия находятся на вашей ответственности и совести! 
      Автор не несет ответственность за ваши действия!
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

SocialKraken 1.2 Beta
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
               
            Snoop - инструмент разведки на основе открытых данных по нику
               snoop
               snoop install
               # https://github.com/snooppr/snoop
               
            Dnnme2 - фейк бот ТГ
               dnnme2
               dnnme2 install
               # гайд -> https://telegra.ph/Sozdaem-bota-dlya-deanonimizacii-04-26
               
            Maltego:
               maltego - запуск
        ''')

      #AhMyth
      elif select == "ahmyth":
         print('\U0001F985' + colr.END + colr.GREEN + ' AhMyth start' + colr.CYAN)
         os.system('gnome-terminal -- bash -c "sudo ahmyth --no-sandbox; exec bash"')
         
      elif select == "ahmyth install":
         print('\U0001F985' + colr.END + colr.GREEN + ' AhMyth install:' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/AhMyth/")
         os.system("python3 ahmyth.py")
      
      #BigBro   
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

      #HiddenEye
      elif select == "hiddeneye":
         print(colr.END + colr.GREEN + ' HiddenEye install:' + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/HiddenEye/HiddenEye")
         os.system("python3 HiddenEye.py")
      
      elif select == "hiddeneye install":
               print(colr.END + colr.GREEN + ' HiddenEye install:'+ colr.CYAN)
               dir = os.getcwd()
               os.chdir(dir + "/modules/HiddenEye/")
               os.system("python3 hiddeneye.py")
      #snoop    
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
          
      #Dnnme2
      elif select == "dnnme2":
         print(colr.END + colr.GREEN + " Start Dnnme2" + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Dnnme2/Dnnme2")
         os.system('gnome-terminal -- bash -c "python3 build.py; exec bash"')
         os.chdir("..")
         os.chdir("..")
         os.chdir("..")
      
      elif select == "dnnme2 install":
         print(colr.END + colr.GREEN + " Start Dnnme2" + colr.CYAN)
         dir = os.getcwd()
         os.chdir(dir + "/modules/Dnnme2/")
         os.system('gnome-terminal -- bash -c "python3 dnnme2.py; exec bash"')
         #os.system("python3 dnnme2.py")
         os.chdir("..")
         os.chdir("..")
         
      #Maltego
      elif select == "maltego":
         print(colr.END + colr.GREEN + '\U0001F441' + ' Maltego start:' + colr.CYAN)
         os.system('gnome-terminal -- bash -c "maltego; exec bash"')
         
      
   
elif (select == 'Нет') or (select == 'нет'): 
   print(colr.BLUE + colr.BOLD + 'Пока ^-^')