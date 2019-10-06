class ListStack:
    def __init__(self):
        self._data = []

    def pop(self):
        return self._data.pop(-1)

    def push(self, item):
        self._data.append(item)

    def print(self):
        print(self._data)


class ArrayStack:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def push(self, item) -> bool:
        if self._size == self._capacity:
            return False
        self._data[self._size] = item
        self._size += 1
        return True

    def pop(self):
        if self._size == 0:
            return None
        val = self._data[self._size-1]
        self._size -= 1
        return val

    def print(self):
        print('current size: ' + str(self._size))
        print(self._data)


stack = ArrayStack(5)
stack.push('bob')
stack.push('alice')
stack.push('daniel')
stack.print()
print(stack.pop())
