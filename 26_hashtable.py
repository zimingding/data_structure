class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Hashtable:
    def __init__(self):
        self._capacity = 8
        self._load_factor = 0.75
        self._size = 0
        self._data = [None] * self._capacity

    def put(self, key, value):
        idx = self.hashcode(key)
        if not self._data[idx]:
            self._size += 1
            if self._size >= self._capacity * self._load_factor:
                self.resize()
            self._data[idx] = ListNode((key, value))
        else:
            curr = self._data[idx]
            prev = None
            while curr:
                if curr.val[0] == key:
                    curr.val = (key, value)
                prev = curr
                curr = curr.next
            prev.next = ListNode((key, value))

    def get(self, key):
        idx = self.hashcode(key)
        if not self._data[idx]:
            return None
        curr = self._data[idx]
        while curr:
            if curr.val[0] == key:
                return curr.val[1]
            curr = curr.next
        return curr

    def resize(self):
        self._capacity *= 2
        table = [None] * self._capacity
        for item in self._data:
            if not item:
                continue
            curr = item
            while curr:
                idx = self.hashcode(curr.val[0])
                if not table[idx]:
                    table[idx] = ListNode(curr.val)
                else:
                    head = table[idx]
                    while head.next:
                        head = head.next
                    head.next = ListNode(curr.val)
                curr = curr.next
        self._data.clear()
        self._data = table

    def hashcode(self, key) -> int:
        h = hash(key)
        return (h ^ (h >> 16)) & (self._capacity - 1)

    def print(self):
        print(self._data)


ht = Hashtable()
ht.put('daniel', 8)
ht.put('tim', 40)
ht.put('vivien', 38)
ht.put('alice', 20)
ht.put('bob', 50)
ht.put('foo', 42)
ht.put('bar', 21)
ht.put('math', 100)
ht.put('english', 100)
ht.put('bob', 99)
ht.print()
print(ht.get('bob'))
