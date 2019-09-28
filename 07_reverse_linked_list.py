class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


