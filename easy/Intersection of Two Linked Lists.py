from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersection = []
        rootB = headB
        while headA != None:
          while headB != None:
            print(headA.val, headB.val)
            if headA.val == headB.val:
              intersection.append(headB.val)
            headB = headB.next
          if headB == None:
            headB = rootB
            print(intersection)
            intersection = []
          headA = headA.next
        
        return None

# [1,9,1,2,4]
# listA = ListNode(1)
# listA.next = ListNode(9)
# listA.next.next = ListNode(1)
# listA.next.next.next = ListNode(2)
# listA.next.next.next.next = ListNode(4)
# [3,2,4]
# listB = ListNode(3)
# listB.next = ListNode(2)
# listB.next.next = ListNode(4)

# [4,1,8,4,5]
listA = ListNode(4)
listA.next = ListNode(1)
listA.next.next = ListNode(8)
listA.next.next.next = ListNode(4)
listA.next.next.next.next = ListNode(5)

# [5,6,1,8,4,5]
listB = ListNode(5)
listB.next = ListNode(6)
listB.next.next = ListNode(1)
listB.next.next.next = ListNode(8)
listB.next.next.next.next = ListNode(4)
listB.next.next.next.next.next = ListNode(5)

# [2,6,4]
# listA = ListNode(2)
# listA.next = ListNode(6)
# listA.next.next = ListNode(4)
# [1,5]
# listB = ListNode(1)
# listB.next = ListNode(5)

solution = Solution()
print(solution.getIntersectionNode(listA, listB))
