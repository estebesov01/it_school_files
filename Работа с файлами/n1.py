# С помощью Linux запишите в Файл все названия 
# директорий из "/" - корневого каталога. Если 
# у вас Windows, сделайте тоже самое))) Только 
# с помощью команды dir. В итоге у вас на рабочем 
# столе должен появиться файл directories.txt. 
# Откройте этот файл с помощью Python и выведите 
# на экран все директории из directories.txt.
ds = '''bin    dev   lib    libx32      mnt   root  snap      sys  var
boot   etc   lib32  lost+found  opt   run   srv       tmp
cdrom  home  lib64  media       proc  sbin  swapfile  usr
'''.split()

with open('Работа с файлами/textfiles/directories.txt','w') as file:
    for i in ds:
        file.write(i + '\n')
with open('Работа с файлами/textfiles/directories.txt','r+') as file:
    print(file.read())