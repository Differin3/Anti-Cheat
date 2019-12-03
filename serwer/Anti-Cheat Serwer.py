import datetime
import socket
import gc
import threading
from colorama import Fore, Back, Style
from colorama import init
init()
if 1 == 1:
        print(Fore.GREEN)
        print("              _-o#&&*''''?d:>bvveev")
        print("          _o/''`''  '',, dMF9MMMMMHoo_")
        print("       .o&#'        `MbHMMMMMMMMMMMHoo-")
        print("     .o"" '         vodM*$&&HMMMMMMMMMMMMM")
        ("    ,'              $M&ood,~'`(&##MMMMMMH")
        print("   /               ,MMMMMMM#b?#bobMMMMHMMML")
        print("  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk")
        print(" ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L")
        print("|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,")
        print("$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?")
        print("]MMH#             ""*""MMM#MMMMMMMMMMMMM'    -")
        print("MMMMMb_                   |MMMMMMMMMMMP'     :")
        print("HMMMMMMMHo                 `MMMMMMMMMT       .")
        print("?MMMMMMMMP                  9MMMMMMMM}       -")
        print("-?MMMMMMM                  |MMMMMMMMM?,d-    '")
        print(" :|MMMMMM-                 `MMMMMMMT .M|.   :")
        print("  .9MMM[                    &MMMMM*' `'    .")
        print("   :9MMk                    `MMM#'        -")
        print("    &M}                     `          .-")
        print("      `&.                             .")
        print("        `~,   .                     ./")
        print("            . _                  .-")
        print("              '`--._,dd###pp=""'")
da = datetime.date.today()
print(da)
log = "log.txt"
myFile = open(log, "w+")  # зоздаёт лог фаил если его не существует
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 1024))
client = []  # Массив где храним адреса клиентов
client1 = str(client)  # Массив
log = (1)  # 1: запесь в лог фаил 0: запись в лог фаил не ведётся
print('Start Server')

while 1:
        data, addres = sock.recvfrom(8128)
        data1 = str(data.decode('utf-8'))  # Массив
        client1 = str(addres)
        if log == 1:
                file = open(r"log.txt", "a")  # открывает лог фаил
                # записывает в лог фаил данные
                file.write(client1 + data1+'\n')
                file.close()
                gc.collect()
        print(addres[0], addres[1])
        print(data.decode('utf-8'))
        if addres not in client:
                # Если такова клиента нету , то добавить
                client.append(addres)
