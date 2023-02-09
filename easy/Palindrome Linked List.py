from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        while head:
            stack.append(head.val)
            head = head.next
        
        if len(stack)%2 == 1:
            return stack[:len(stack)//2] == list(reversed(stack[len(stack)//2+1:]))
        else:
            return stack[:len(stack)//2] == list(reversed(stack[len(stack)//2:]))

# [1,2,2,1]
# [1,2,3,2,1]
# [1,2,3]
solution = Solution()
print(solution.isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1))))))
print(solution.isPalindrome(ListNode(1,ListNode(2,ListNode(3,ListNode(2,ListNode(1)))))))
print(solution.isPalindrome(ListNode(1,ListNode(2,ListNode(3)))))
