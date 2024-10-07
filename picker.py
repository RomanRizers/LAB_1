from employee import Employee

class Picker(Employee):
    def __post_init__(self):
        super().__post_init__()
        self.zone = ""

    def read(self):
        super().read()
        self.zone = self.io.input('Зона сборки')

    def write(self):
        super().write()
        self.io.output('Зона сборки', self.zone)
