class ListQueue:
    def __init__(self):
        self._data = []

    def put(self, item):
        self._data.append(item)

    def get(self):
        return self._data.pop(0)

    def print(self):
        print(self._data)


class ArrayQueue:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._data = [None] * capacity
        self._head = 0
        self._tail = 0

    def put(self, item) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False

            for i in range(self._tail - self._head):
                self._data[i] = self._data[i + self._head]

            self._tail -= self._head
            self._head = 0
        self._data[self._tail] = item
        self._tail += 1
        return True

    def get(self):
        if self._head == self._tail:
            return None
        val = self._data[self._head]
        self._head += 1
        return val

    def print(self):
        print('head: ' + str(self._head) + ', tail: ' + str(self._tail))
        print(self._data)


queue = ArrayQueue(10)
for i in range(10):
    queue.put(i)
for i in range(10):
    print(queue.get())
queue.print()
queue.put(42)
queue.print()