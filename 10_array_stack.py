class ArrayStack:
    def __init__(self):
        self._data = []

    def pop(self):
        return self._data.pop(-1)

    def push(self, item):
        self._data.append(item)

    def print(self):
        print(self._data)


stack = ArrayStack()
stack.push('bob')
stack.push('alice')
stack.push('daniel')
stack.print()
print(stack.pop())
