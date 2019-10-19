class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class CycleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, node: ListNode):
        if not self.head:
            self.head = node
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = node
            node.next = self.head

    def remove(self, node: ListNode):
        prev = None
        curr = self.head
        while curr.val != node.val:
            prev = curr
            curr = curr.next
        if not prev:
            tail = self.head
            while tail.next.val != self.head.val:
                tail = tail.next
            if self.head.val == tail.val:
                self.head = None
            else:
                self.head = self.head.next
                tail.next = self.head
        else:
            prev.next = curr.next

    def print(self):
        if not self.head:
            return

        curr = self.head
        print(curr.val)
        while curr.next != self.head:
            curr = curr.next
            print(curr.val)


cycle_list = CycleLinkedList()
cycle_list.add(ListNode(1))
cycle_list.add(ListNode(2))
cycle_list.add(ListNode(3))
cycle_list.print()
cycle_list.remove(ListNode(1))
cycle_list.remove(ListNode(3))
cycle_list.remove(ListNode(2))
cycle_list.print()
