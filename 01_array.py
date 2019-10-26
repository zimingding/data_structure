# dynamic array, automatic resize
class Array:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def add(self, index: int, element: int):
        if index < 0 or index > self._size:
            raise Exception('Invalid index: {}'.format(index))

        if self._size == self._capacity:
            new_capacity = int(self._capacity * 1.5)
            self.resize(new_capacity)

        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]

        self._data[index] = element
        self._size += 1

    def resize(self, new_capacity):
        new_arr = Array(new_capacity)
        for i in range(self._size):
            new_arr.add(i, self._data[i])
        self._capacity = new_capacity
        self._data = new_arr._data

    def print(self):
        print(self._data)


a = Array()
for i in range(10):
 a.add(i, i + 1)
a.print()

a.add(3, 100)
a.print()