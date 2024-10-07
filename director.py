from employee import Employee

class Director(Employee):
    def __init__(self, id):
        super().__init__(id)

    def read(self):
        super().read()

    def write(self):
        super().write()
        
