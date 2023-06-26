from collections import Counter  
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_counter = Counter(nums) 
        zeros_count = nums_counter[0] 
        ones_index = nums_counter[1] + nums_counter[0]
        nums[: nums[0]] = [0 for _ in range(nums_counter[0])]
        nums[zeros_count: ones_index] = [1 for _ in range(nums_counter[1])]
        nums[ones_index: ] = [2 for _ in range(nums_counter[2])]