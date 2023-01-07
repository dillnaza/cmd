import os
import datetime

filename = 'C:\\'
s_prev = 'C:\\'
s = 'C:\\'

while True:
    command = input(s + '>')
    if command == 'dir' or command == 'ls':
        print(f'Содержимое папки {s}\n')
        dir = os.listdir(s)
        count_file = 0
        count_dir = 0
        size_file = 0
        size_dir = 0
        for i in dir:
            print(datetime.datetime.fromtimestamp(int(os.path.getctime(s + '\\' + i))), '   ', i)
            if os.path.isdir(s + i):
                count_dir = count_dir + 1
                size_dir = size_dir + os.path.getsize(s + '\\' + i)
            if os.path.isfile(s + i):
                count_file = count_file + 1
                size_file = size_file + os.path.getsize(s + '\\' + i)
        print('            ', count_file, 'файлов', size_file, 'байт')
        print('            ', count_dir, 'папок', size_dir, 'байт')
    if command[0] == 'c' and command[1] == 'd' and command[2] == ' ':
        filename = command[3:] + '\\'
        if os.path.isdir(s + '\\' + command[3:]):
            s = s + filename
        elif os.path.isfile(s + command[3:]):
            s = s + '\\' + command[3:]
            print('Размер:', os.path.getsize(s) // 1024, 'Кб')
            print('Дата создания:',
                  datetime.datetime.fromtimestamp(
                      int(os.path.getctime(s))))
            print('Дата последнего открытия:',
                  datetime.datetime.fromtimestamp(
                      int(os.path.getatime(s))))
            print('Дата последнего изменения:',
                  datetime.datetime.fromtimestamp(
                      int(os.path.getmtime(s))))
            s = s + '\\'
        else:
            print('Системе не удается найти указанный путь.')
    if command[0] == 'c' and command[1] == 'd' and command[2] == '.' and command[3] == '.':
        s_prev = s[::-1]
        s = s_prev[s_prev.find("\\") + 1:]
        s = s[::-1]
        s_prev = s[::-1]
        s = s_prev[s_prev.find("\\") + 1:]
        s = s[::-1] + "\\"
    if command[0:5] == 'mkdir':
        if os.path.isdir(s + '\\' + command[6:]):
            print(f'Папка/файл с именем {command[6:]} уже существует в данной директории')
        else:
            os.mkdir(s + '\\' + command[6:])
    if command[0:5] == 'rmdir':
        if os.path.isdir(s + '\\' + command[6:]):
            os.rmdir(s + '\\' + command[6:])
        else:
            print(f'Папка/файл с именем {command[6:]} не существует в данной директории')
    if command[0:6] == 'rename':
        s_prev, s_sled = command[6:].split()
        if os.path.isdir(s+'\\'+s_prev):
            os.rename(s+'\\'+s_prev,s+'\\'+s_sled)
        else:
            print(f'Папка/файл с именем {s_prev} не существует в данной директории')
