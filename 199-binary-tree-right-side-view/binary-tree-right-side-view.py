# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    #Level order traverse (BFS) 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        ans = []
        q = collections.deque([root])

        while q:
            right_element = None
            q_len = len(q)

            #removing previous leve elemnts then adding elements of the next element
            for level in range(q_len):
                node = q.popleft()
                if node:
                    right_element = node
                    q.append(node.left)
                    q.append(node.right) 

            if right_element:
                ans.append(right_element.val) 
        return ans
                    