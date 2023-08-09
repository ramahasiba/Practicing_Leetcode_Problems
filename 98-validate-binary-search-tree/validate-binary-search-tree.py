# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(lower, upper, root):
    if not root:
        return True
    elif root.val <= lower or root.val >= upper:
        return False
    else:
        return dfs(lower, root.val, root.left) and dfs(root.val, upper, root.right)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return dfs(float('-inf'), float('inf'), root)