from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        stack.pop(-n)
        if len(stack) == 0:
            return None
        v = stack.pop(0)
        cur = start = ListNode(v)
        while len(stack) > 0:
            v = stack.pop(0)
            cur.next = ListNode(v)
            cur = cur.next
        return start

# head = [1,2,3,4,5], n = 2
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

solution = Solution()
l = solution.removeNthFromEnd(head, 2)
print(l.val)
print(l.next.val)
print(l.next.next.val)
print(l.next.next.next.val)

# head = [1], n = 1
head = ListNode(1)
l = solution.removeNthFromEnd(head, 1)
print(l.val)

# head = [1,2], n = 1
head = ListNode(1,ListNode(2))
l = solution.removeNthFromEnd(head, 1)
print(l.val)
