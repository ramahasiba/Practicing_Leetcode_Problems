# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next 

        left_ptr, right_ptr = 0, len(nums) - 1
        while left_ptr <= right_ptr:
            if nums[left_ptr] != nums[right_ptr]:
                return False
            left_ptr += 1
            right_ptr -= 1
        return True
