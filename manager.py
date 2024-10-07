from employee import Employee

class Manager(Employee):
    def __post_init__(self):
        super().__post_init__()
        self.department = ""

    def read(self):
        super().read()
        self.department = self.io.input('Отдел')

    def write(self):
        super().write()
        self.io.output('Отдел', self.department)
        