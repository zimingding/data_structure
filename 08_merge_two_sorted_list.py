class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            else:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
