from dataclasses import dataclass
from console_io import ConsoleIO

@dataclass
class Employee:
    id: int = 0
    name: str = ""
    age: int = 0
    experience: str = ""

    def __post_init__(self):
        self.io = ConsoleIO()

    def read(self):
        self.name = self.io.input('Имя:')
        self.age = int(self.io.input('Возраст:'))
        self.experience = int(self.io.input('Стаж работы:'))

    def write(self):
        self.io.output('ID', self.id)
        self.io.output('Имя', self.name)
        self.io.output('Возраст', self.age)
        self.io.output('Стаж работы', self.experience)

