"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue =deque()
        result = []

        if not root:
            return result
        
        # result.append([root.val])
        queue.append(root)

        while len(queue):
            level = []

            current_nodes =len(queue)

            for _ in range(current_nodes):
                tmp = queue.popleft()
                level.append(tmp.val)
                for child in tmp.children:
                    queue.append(child)
            result.append(level)

        return result

        
