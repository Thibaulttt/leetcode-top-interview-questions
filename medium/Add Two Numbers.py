from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # stack1 = stack2 = []
        # while l1:
        #     stack1.insert(0, l1.val)
        #     l1 = l1.next
        
        # print(stack1)

        n1 = n2 = ""
        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next
        
        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next
        
        res = int(n1) + int(n2)

        cur = start = ListNode()
        for e in reversed(str(res)):
            cur.next = ListNode(e)
            cur = cur.next

        return start.next

solution = Solution()

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(solution.addTwoNumbers(l1, l2).val)
print(solution.addTwoNumbers(l1, l2).next.val)
print(solution.addTwoNumbers(l1, l2).next.next.val)

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]