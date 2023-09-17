# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # root -> left -> right 
        q = collections.deque([root]) 
        answer = []

        while q: 
            q_len = len(q) 
            level_vals = []
            #removing previous leve elemnts then adding elements of the next element
            for level in range(q_len):
                node = q.popleft()
                if node:
                    level_vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right) 
            if level_vals:
                answer.insert(0, level_vals)

        return answer

             