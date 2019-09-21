class Array:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None]*capacity

    def add(self, element: int):
        if self._size == self._capacity:
            raise Exception('No more space for new element')

        idx = 0
        while idx < self._size:
            if self._data[idx] >= element:
                break
            else:
                idx += 1

        for i in range(self._size-1, idx - 1, -1):
            self._data[i+1] = self._data[i]

        self._data[idx] = element
        self._size += 1

    def delete(self, idx: int):
        if idx < 0 or idx >= self._size:
            raise Exception('Invalid index: {}'.format(idx))

        for i in range(idx, self._size-1):
            self._data[i] = self._data[i+1]
        self._data[self._size-1] = None
        self._size -= 1

    def update(self, idx: int, element: int):
        self.delete(idx)
        self.add(element)

    def print(self):
        print(self._data)


array = Array()
array.add(1)
array.add(3)
array.add(2)
array.add(8)
array.add(5)
array.add(7)
array.add(9)
array.add(4)
array.add(6)
array.add(10)
array.print()
array.delete(0)
array.delete(1)
array.print()
array.update(0, 2)
array.print()
array.update(3, 0)
array.print()