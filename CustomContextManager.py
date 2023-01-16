import os


class CustomContextManager:
    s = 'C:\\'
    commands = ''
    road = ''

    def __init__(self):
        commands = input(self.getS() + self.getRoad() + '>')
        self.setCommands(commands)

    def __enter__(self):
        if self.commands[:4] == 'dir':
            self.commandDir()
        if self.commands[:3] == 'cd ':
            self.commandCd()
        if self.commands[:5] == 'cd.. ':
            self.commandCdpp()
        if self.commands[:5] == 'open ':
            self.commandOpen()
        if self.commands[:6] == 'mkdir ':
            self.commandMkdir()
        if self.commands[:6] == 'rmdir ':
            self.commandRmdir()
        if self.commands[:7] == 'rename ':
            self.commandRename()

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    def getCommands(self) -> str:
        return self.commands

    def setCommands(self, commands: str):
        self.commands = commands

    def getRoad(self) -> str:
        return self.road

    def setRoad(self, road: str):
        self.road = road

    def getS(self):
        return self.s

    def commandDir(self):
        with os.scandir(self.s) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(entry.name)

    def commandCd(self):
        name = self.commands[3:]
        self.setRoad(os.path.join(self.road, name))

    def commandCdpp(self):
        name = self.commands[5:]
        self.setRoad(os.path.split(self.road)[0])

    def commandOpen(self):
        print('open')

    def commandMkdir(self):
        try:
            os.mkdir(self.getS() + self.getRoad() + self.commands[6:])
        except FileExistsError:
            print(f'Подпапка или файл  {self.commands[6:]} уже существует.')

    def commandRmdir(self):
        try:
            os.rmdir(self.getS() + self.getRoad() + self.commands[6:])
            print(self.getS() + self.getRoad() + self.commands[6:])
        except FileNotFoundError:
            print(f'Не удается найти указанный файл.')

    def commandRename(self):
        name_old, name_new = self.commands[6:].split()
        try:
            os.rename(self.getS() + name_old, self.getS() + name_new)
        except:
            print(f'Не удается найти указанный файл.')
