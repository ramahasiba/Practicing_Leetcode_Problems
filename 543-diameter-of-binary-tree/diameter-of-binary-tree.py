# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(root: Optional[TreeNode]) -> int: 
        return max(
            (maxDepth(root.left),
            maxDepth(root.right))
        ) +1 if root else 0

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        self.diameterOfBinaryTree(root.right)
        self.diameterOfBinaryTree(root.left)
          
        right_max_depth = maxDepth(root.right) 
        left_max_depth = maxDepth(root.left)

        self.diameter = max(self.diameter, (right_max_depth + left_max_depth))

        return self.diameter 