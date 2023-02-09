from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    s = 0
    for n in head:
      s += n.val
    return s > 0

# Input: head = [3,2,0,-4], pos = 1

l = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))

solution = Solution()
print(solution.hasCycle(l))