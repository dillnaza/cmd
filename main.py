from CustomContextManager import CustomContextManager

print("""Microsoft Windows [Version 10.0.19044.2486]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.""")


while True:
    with CustomContextManager() as f:
        ...
