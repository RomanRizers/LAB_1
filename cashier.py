from employee import Employee

class Cashier(Employee):
    def __post_init__(self):
        super().__post_init__()
        self.shift = ""

    def read(self):
        super().read()
        self.shift = self.io.input('Смена')

    def write(self):
        super().write()
        self.io.output('Смена', self.shift)
        
