import pickle

class PickleStorage:
    def __init__(self, container):
        self.container = container

    def store(self):
        with open("data.dat", "wb") as f:
            pickle.dump((self.container.maxID, self.container.items), f)

    def load(self):
        with open("data.dat", "rb") as f:
            self.container.maxID, self.container.items = pickle.load(f)
