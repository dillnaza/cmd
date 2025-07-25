import os
import datetime

s = 'C:\\'

def commandDir(s: str):
    count_file = 0
    count_dir = 0
    size_file = 0
    size_dir = 0
    print(f'Содержимое папки {s}\n')
    with os.scandir(s) as entries:
        for entry in entries:
            road = os.path.join(os.path.join(s, entry.name))
            if os.path.isdir(road):
                count_dir += 1
                size_dir += os.path.getsize(road)
                print(datetime.datetime.fromtimestamp(int(os.path.getctime(road))),
                      '<DIR>'.center(25), entry.name)
            if os.path.isfile(road):
                count_file += 1
                size_file += + os.path.getsize(road)
                print(datetime.datetime.fromtimestamp(int(os.path.getctime(road))),
                      str(os.path.getsize(road)).rjust(25), entry.name)
        print('            ', count_file, 'файлов', size_file, 'байт')
        print('            ', count_dir, 'папок', size_dir, 'байт')

def commandCd(command: str, s: str) -> str:
    s = os.path.join(s, command)
    if os.path.isfile(s):
        try:
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
        except FileNotFoundError:
            print('Системе не удается найти указанный путь.')
    return s

def commandCdpp(s: str) -> str:
    s = os.path.split(s)[0]
    return s

def commandOpen(command: str):
    try:
        with open(s + '\\' + command, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('Системе не удается найти указанный путь.')

def commandMkdir(command: str):
    try:
        os.mkdir(s + '\\' + command)
    except FileExistsError:
        print(f'Подпапка или файл  {command} уже существует.')

def commandRmdir(command: str):
    try:
        os.rmdir(s + '\\' + command)
    except FileNotFoundError:
        print(f'Не удается найти указанный файл.')

def commandRename(command: str):
    name_old, name_new = command.split()
    try:
        os.rename(s + '\\' + name_old, s + '\\' + name_new)
    except FileNotFoundError:
        print(f'Не удается найти указанный файл.')

while True:
    command = input(s + '>')
    if command[:4] == 'dir':
        commandDir(s)
    elif command[:3] == 'cd ':
        s = commandCd(command[3:], s)
    elif command[:4] == 'cd..':
        s = commandCdpp(s)
    elif command[:5] == 'open ':
        commandOpen(command[5:])
    elif command[:6] == 'mkdir ':
        commandMkdir(command[6:])
    elif command[:6] == 'rmdir ':
        commandRmdir(command[6:])
    elif command[:7] == 'rename ':
        commandRename(command[7:])
    else:
        print(f'{command} не является внутренней или внешней командой, исполняемой программой или пакетным файлом')
