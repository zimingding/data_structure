from typing import List


class MinHeap:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._a = [None]*(self._capacity+1)
        self._size = 0

    def insert(self, data: int):
        if self._size == self._capacity:
            return

        self._size += 1
        self._a[self._size] = data
        i = self._size
        while int(i/2) > 0 and self._a[int(i/2)] > self._a[i]:
            self._a[int(i/2)], self._a[i] = self._a[i], self._a[int(i/2)]
            i = int(i/2)

    def removeMin(self):
        if self._size == 0:
            return

        self._a[1] = self._a[self._size]
        self._a[self._size] = None
        self._size -= 1
        self.heapify()

    def heapify(self):
        i = 1
        while True:
            minPos = i
            if i*2 < self._size and self._a[i*2] < self._a[i]:
                minPos = i*2
            if i*2+1 < self._size and self._a[i*2+1] < self._a[minPos]:
                minPos = i*2+1
            if minPos == i:
                break
            self._a[i], self._a[minPos] = self._a[minPos], self._a[i]
            i = minPos

    def getMin(self) -> int:
        return self._a[1]

    def getData(self) -> List[int]:
        return self._a[1:]
