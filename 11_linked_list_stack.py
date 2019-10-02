class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListStack:
    def __init__(self):
        self._head = None

    def push(self, item):
        if not self._head:
            self._head = ListNode(item)
        else:
            head = ListNode(item)
            head.next = self._head
            self._head = head

    def pop(self):
        value = self._head.val
        self._head = self._head.next
        return value


stack = LinkedListStack()
stack.push('alice')
stack.push('bob')
stack.push('leo')
print(stack.pop())
