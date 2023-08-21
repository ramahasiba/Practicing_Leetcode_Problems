# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def findPath(root: TreeNode, target: int) -> List[int]:
    path = []
    dfs(root, target, path)
    return path
def dfs(node, target, path):
    if not node:
        return False 
    # Add the current node's value to the path
    path.append(node.val) 
    if node.val == target:
        return True 
    if dfs(node.left, target, path) or dfs(node.right, target, path):
        return True 
    # Remove the current node's value from the path if the target is not found
    path.pop()
    return False 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        p_path = findPath(root, p.val)
        q_path = findPath(root, q.val) 
        intersection = [x for x in p_path if x in q_path]
        if intersection:
            return TreeNode(intersection[-1])
        else:
            return root 