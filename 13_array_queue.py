class ArrayQueue:
    def __init__(self):
        self._data = []

    def put(self, item):
        self._data.append(item)

    def get(self):
        return self._data.pop(0)

    def print(self):
        print(self._data)


queue = ArrayQueue()
queue.put('bob')
queue.put('alice')
queue.put('daniel')
queue.print()
print(queue.get())
print(queue.get())
print(queue.get())
