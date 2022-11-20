from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty


class Storage(ABC):
    def __init__(self, items: dict[str:int], capacity: int):
        self._items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass


class Store(Storage):

    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def add(self, name, count):
        data = self.items
        if not data.get(name, None):
            data[name] = count
        else:
            data[name] += count
        self.items = data

    def remove(self, name, count):
        data = self.items
        data[name] -= count
        if data[name] == 0:
            del data[name]
        self.items = data

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value


class Shop(Storage):

    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        data = self.items
        if not data.get(name, None):
            data[name] = count
        else:
            data[name] += count
        self.items = data

    def remove(self, name, count):
        data = self.items
        data[name] -= count
        if data[name] == 0:
            del data[name]
        self.items = data

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value


class Request:
    def __init__(self, data):
        self.amount = int(data[1])
        self.product = data[2]
        self.fromm = data[4]
        self.to = data[-1]
