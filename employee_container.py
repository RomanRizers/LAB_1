from employee import Employee
from manager import Manager
from cashier import Cashier
from picker import Picker
from director import Director
from pickle_storage import PickleStorage

class EmployeeContainer:
    def __init__(self):
        self.items = {}
        self.storage = PickleStorage(self)
        self.maxID = 0

    def add(self):
        print("\n" + "-" * 40)
        print("Выберите должность:")
        print("1. Менеджер")
        print("2. Кассир")
        print("3. Сборщик")
        print("4. Директор")
        print("-" * 40 + "\n")
        
        try:
            choice = int(input("Введите номер должности: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
            return

        if choice == 1:
            employee = Manager(id=self.maxID + 1)
        elif choice == 2:
            employee = Cashier(id=self.maxID + 1)
        elif choice == 3:
            employee = Picker(id=self.maxID + 1)
        elif choice == 4:
            employee = Director(id=self.maxID + 1)
        else:
            print("Некорректный выбор")
            return

        employee.read()
        self.items[employee.id] = employee
        self.maxID += 1
        print("\nСотрудник успешно добавлен!\n" + "-" * 40)
        
    def write(self):
        print("\n" + "-" * 40)
        for employee in self.items.values():
            employee.write()
            print("-" * 40)

    def store(self):
        self.storage.store()
        print("\nДанные успешно сохранены!\n")

    def load(self):
        self.storage.load()
        print("\nСписок загружен.")
    
    def update(self):
        print("\n" + "-" * 40)
        id = int(input("Введите ID сотрудника для обновления: "))
        if id in self.items:
            
            print("\nТекущие данные сотрудника:")
            self.items[id].write()
            
            print("\nВведите новые данные для сотрудника:")
            self.items[id].read()
            
            print("\nДанные сотрудника обновлены.")
        else:
            print("Сотрудник с данным ID не найден.")

    def delete(self):
        print("\n")
        id = int(input("Введите ID для удаления: "))
        if id in self.items:
            del self.items[id]
            print("Сотрудник удалён.\n")
        else:
            print("Сотрудник не найден.")
