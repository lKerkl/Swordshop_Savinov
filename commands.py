import classes

class AddCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        self.productStorage.storage.append(classes.Product(params[0], params[1]))
    def __str__(self):
        return " Команда добавление. Пример: add НазваниеТовара Цена"
class ListCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        for x in self.productStorage.storage:
            print(x)
    def __str__(self):
        return " Список продуктов. Пример: list"

class DeleteCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        self.productStorage.storage.pop(int(params[0]))
    def __str__(self):
        return " Команда удаления. Пример: delete НазваниеТовара"

class HelpCommand:
    def __init__(self, prorab: classes.Prorab):
        self.prorab = prorab
    def __str__(self):
        return " Список команд. Пример: help"

    def execute(self, params: []):
        for i in self.prorab.spisok.keys():
            print(i, str(self.prorab.spisok[i]))

class QuitCommand:
    def __init__(self):
        pass
    def execute(self, params: []):
            print("Выход")
            quit()
    def __str__(self):
        return " Выход. Пример: quit"

