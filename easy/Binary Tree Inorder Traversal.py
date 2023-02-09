from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
  # (or preorder) Node, left, right
  def recursive_dfs(self, node: Optional[TreeNode]):
    yield node.val
    if node.left != None:
      yield from self.recursive_dfs(node.left)
    if node.right != None:
      yield from self.recursive_dfs(node.right)

  def non_recursive_dfs(self, node: Optional[TreeNode]):
    res = []
    stack = set()
    stack.add(node)
    if node == None:
      return res

    while len(stack) > 0:
      cur_node = stack.pop()

      if cur_node not in res:
        res.append(cur_node)
      
      if cur_node.left != None:
        stack.add(cur_node.left)

      if cur_node.right != None:
        stack.add(cur_node.right)

      print([o.val for o in stack])
    return res

  # Left, node, right
  def recursive_inorder(self, node: Optional[TreeNode]) -> List[int]:
    if node.left != None:
      yield from self.recursive_inorder(node.left)
    yield node.val
    if node.right != None:
      yield from self.recursive_inorder(node.right)

  def non_recursive_inorder(self, node: Optional[TreeNode]) -> List[int]:
    res = []
    stack = set()
    if node == None:
      return res

    stack.add(node.left)
    stack.add(node.right)

    while len(stack) > 0:
      node1 = stack.pop()

      if node1 != None:
        print(node1.val)
        stack.add(node1.left)
        res.append(node1.val)
        stack.add(node1.right)

    return res

  # Left, right, node
  def recursive_postorder(self, node: Optional[TreeNode]) -> List[int]:
    if node.left != None:
      yield from self.recursive_postorder(node.left)
    if node.right != None:
      yield from self.recursive_postorder(node.right)
    yield node.val
  
  def non_recursive_postorder(self, node: Optional[TreeNode]) -> List[int]:
    pass

solution = Solution()

# root = TreeNode(1, TreeNode(), TreeNode(2, TreeNode(3), TreeNode()))
# [1,2,2,3,4,4,3,5,6,5,6,6,5,6,5]
root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5), TreeNode(6)), TreeNode(4, TreeNode(5), TreeNode(6))), TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(5))))


print(list(solution.recursive_dfs(root)))
print([o.val for o in list(solution.non_recursive_dfs(root))])
print()

# print(list(solution.recursive_inorder(root)))
# print(solution.non_recursive_inorder(root))
# print()

solution.recursive_postorder(TreeNode(1, TreeNode(), TreeNode(2, TreeNode(3), TreeNode())))
