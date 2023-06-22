class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums) 
        zeros_count = nums.count(0)
        ones_count = nums.count(1)
        twos_count = nums.count(2)  
        nums[: zeros_count] = [0 for _ in range(zeros_count)]
        ones_index = ones_count + zeros_count
        nums[zeros_count: ones_index] = [1 for _ in range(ones_count)]
        nums[ones_index: ] = [2 for _ in range(twos_count)]