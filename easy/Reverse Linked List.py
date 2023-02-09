from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        cur = start = ListNode()
        for e in reversed(stack):
            cur.next = ListNode(e)
            cur = cur.next

        return start.next

# [1,2,3,4,5]
solution = Solution()
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(solution.reverseList(l).next.val)

# [1,2]

# [1]

# []