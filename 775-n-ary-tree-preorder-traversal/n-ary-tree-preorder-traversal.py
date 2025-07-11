"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        self.traverse(root, result)

        return result

    def traverse(self, tree, result):
        if tree:
            result.append(tree.val)
            for child in tree.children:
                self.traverse(child, result)
        