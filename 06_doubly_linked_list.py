class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, node: ListNode):
        if not self.head:
            self.head = node
            self.head.next = None
            self.head.prev = None
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            node.prev = curr
            node.next = None
            curr.next = node

    def remove(self, node: ListNode):
        curr = self.head
        while curr.val != node.val:
            curr = curr.next
        if not curr.prev:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            curr.prev.next = curr.next

    def print(self):
        curr = self.head
        while curr:
            print('current node: ' + str(curr.val) +
                  ', prev node: ' + (str(curr.prev.val) if curr.prev else 'None') +
                  ', next node: ' + (str(curr.next.val) if curr.next else 'None'))
            curr = curr.next


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.add(ListNode(1))
doubly_linked_list.add(ListNode(2))
doubly_linked_list.add(ListNode(3))
doubly_linked_list.print()
doubly_linked_list.remove(ListNode(1))
doubly_linked_list.print()
doubly_linked_list.remove(ListNode(3))
doubly_linked_list.remove(ListNode(2))
doubly_linked_list.print()
