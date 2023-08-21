# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## left -> node -> right 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.tree_values = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.tree_values.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.tree_values

        
        
