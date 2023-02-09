from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    stack_left = set()
    stack_right = set()
    if root == None:
      return True
    
    if root.left.val != root.right.val:
      return False
    
    stack_left.add(root.left)
    stack_right.add(root.right)

    while len(stack_left) > 0 and len(stack_right) > 0:
      cur_node_left = stack_left.pop()
      cur_node_right = stack_right.pop()

      if cur_node_left != None and cur_node_right != None:
        stack_right.add(cur_node_right.right)
        stack_right.add(cur_node_right.left)
        stack_left.add(cur_node_left.right)
        stack_left.add(cur_node_left.left)
        print(cur_node_left.val, cur_node_right.val)

    return True

# [1,2,2,3,4,4,3]
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))

# [1,2,2,3,4,4,3,5,6,5,6,6,5,6,5]
root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5), TreeNode(6)), TreeNode(4, TreeNode(5), TreeNode(6))), TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(5))))

solution = Solution()
print(solution.isSymmetric(root))
