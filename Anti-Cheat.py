#импорт
import subprocess
import time
import os
import gc
import zlib
import socket
import threading
# переменные
process_name = "csgo.exe"  # н звание процесса
signatures  = "" # сигнатуры
mode = 1 # режим
v = "0.8" # версия
scan_delay = 5 # время
taem_delay = 10  # время до запуска
port = 1024 # порт подключения
ser = "192.168.0.102"
server = ser, + port
if os.path.isfile("sig.txt"):
    os.remove("sig.txt")
# start
print("Start anti-Cheat")
time.sleep(1)
iogin = open("C:\Program Files (x86)\Steam\config\loginusers.vdf", "r")
ID = iogin.readlines()[2]
print("SteamID:", ID)
# серверная часть
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))  # Задаем сокет как клиент
sor.sendto((ID +' Connect server').encode('utf-8'), server)  # Уведомляем
print("connect  serwer")
# проверка
if os.path.isfile("Listdlls.exe"):
    mode = 1
else:
    print("ERROR Не найден фаил Listdlls.exe")
    mode = 0
    taem_delay = 0
# Загрузка
if 10 == taem_delay:
    print("loanding... 10%")
    time.sleep(1)
    print("loanding... 20%")
    time.sleep(1)
    print("loanding... 30%")
    time.sleep(1)
    print("loanding... 40%")
    time.sleep(1)
    print("loanding... 50%")
    time.sleep(1)
    print("loanding... 60%")
    time.sleep(1)
    print("loanding... 70%")
    time.sleep(1)
    print("loanding... 80%")
    time.sleep(1)
    print("loanding... 90%")
    time.sleep(1)
    print("loanding...100%")
r = ('Listdlls ' + process_name)
print(r)
# Функции
def crc(fileName):
    prev = 0
    for eachLine in open(fileName, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)
# Имплементация
sigs_path = process_name + "_sigs.txt"
sigs_local_path = "./sig.txt"
if mode:
    # создание сигнатур
    sigs = subprocess.check_output(r).decode("UTF-8")
    f = open(sigs_path, 'w')
    f.write( sigs )
    f.close()

    print("Сигнатуры процесса " + process_name + " созданы")

    # проверка по сигнатурам
    f = open(sigs_local_path, 'w')
    f.write( sigs )
    f.close()

    while True:
        print("Сканирую игру... ")
        sigs = subprocess.check_output(r).decode("UTF-8")
        f = open(sigs_local_path, 'w')
        f.write( sigs )
        f.close()

        check = crc(sigs_path) == crc(sigs_local_path)
        mensahe = check 
        if( check ):
            # Сигнатуры совпали
            print( "Сигнатуры совпали, продолжаю... ")
            time.sleep(scan_delay)
            continue
        else:
            # Сигнатуры не совпали
            print("Сигнатуры не совпали, закрываю игру ")
            os.remove(sigs_path)
            # отправака покетов данных
            sor.sendto((ID + " cигнатуры не совпали").encode('utf-8'), server)
            os.system('TASKKILL /f /im ' + process_name)

print("античит v"+v+" завершил работу.")
