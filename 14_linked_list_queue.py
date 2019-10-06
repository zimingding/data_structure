class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None

    def put(self, item):
        if not self.head:
            self.head = ListNode(item)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(item)

    def get(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


queue = LinkedListQueue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.print()
print(queue.get())
print(queue.get())
print(queue.get())
