class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node: ListNode):
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def remove(self, node: ListNode):
        prev = None
        curr = self.head
        while curr.val != node.val:
            prev = curr
            curr = curr.next
        if not prev:
            self.head = self.head.next
        else:
            prev.next = curr.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


linked_list = LinkedList()
linked_list.add(ListNode(1))
linked_list.add(ListNode(2))
linked_list.add(ListNode(3))
linked_list.print()
linked_list.remove(ListNode(1))
linked_list.remove(ListNode(3))
linked_list.remove(ListNode(2))
linked_list.print()
