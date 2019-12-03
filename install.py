from zipfile import ZipFile
import os 
import requests #импортируем модули
update = 1
file_name = "update.zip"
v = "0.8"  # версия
if update == 1:
    f = open(r'update.zip', "wb")  # открываем файл для записи, в режиме wb
    ufr = requests.get("https://github.com/Differin3/Anti-Cheat/archive/master.zip") #делаем запрос
    print("Download..")
    f.write(ufr.content) #записываем содержимое в файл; как видите - content запросаИзвлечь все файлы
    f.close()

    with ZipFile(file_name, 'r') as zip:
    
        zip.printdir()

        print('Извлечение всех файлов....')
        zip.extractall()
        print('Done!')
        zip.close()
        os.remove(file_name)
