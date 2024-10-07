from employee_container import EmployeeContainer

def main():
    container = EmployeeContainer()
    
    menu = [
        ["Добавить сотрудника", container.add],
        ["Удалить сотрудника", container.delete],
        ["Обновить данные сотрудника", container.update],
        ["Показать всех сотрудников", container.write],
        ["Сохранить в файл", container.store],
        ["Загрузить из файла", container.load],
        ["Выход", exit],
    ]

    while True:
        print("\n" + "-" * 40)
        print("Меню:")
        for i, menuItem in enumerate(menu, 1):
            print(f"{i}. {menuItem[0]}")
        print("-" * 40) 
        
        try:
            print("\n")
            m = int(input("Выберите действие: "))
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")
            continue
        
        if 1 <= m <= len(menu):
            menu[m-1][1]()
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
