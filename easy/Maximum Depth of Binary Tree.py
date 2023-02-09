from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def bfs(self, root: Optional[TreeNode]):
    res = []
    stack = [root]

    while len(stack) > 0:
      cur_node = stack.pop()
      res.append(cur_node.val)
      if cur_node.left != None:
        stack.append(cur_node.left)
      
      if cur_node.right != None:
        stack.append(cur_node.right)
    
    return res
  
  def dfs(self, root: Optional[TreeNode]):
    res = []
    stack = [root]
    depth = 0

    while len(stack) > 0:
      cur_node = stack.pop()
      res.append(cur_node.val)
      if cur_node.left != None:
        stack.insert(-1, cur_node.left)

      if cur_node.right != None:
        stack.insert(-1, cur_node.right)
      if depth < len(stack):
        depth = len(stack)
      
    
    return res, depth

  def maxDepth(self, root: Optional[TreeNode]) -> int:
    pass

solution = Solution()
tree = TreeNode(1, TreeNode(), TreeNode(2, TreeNode(3), TreeNode()))
print(solution.bfs(tree))
print(solution.dfs(tree))