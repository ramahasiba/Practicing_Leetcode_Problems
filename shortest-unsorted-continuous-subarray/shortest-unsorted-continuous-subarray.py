class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int: 
        nums_length = len(nums)
        first_ptr, second_ptr = nums_length, 0  
        sorted_nums = nums.copy()
        sorted_nums.sort()

        for index, num in enumerate(nums):
            if nums[index] != sorted_nums[index]:
                first_ptr = min(first_ptr, index)
                second_ptr = max(second_ptr, index)
        if first_ptr == second_ptr:
            return 0
        else:
            return len(nums[first_ptr: second_ptr + 1])


        return len(nums[subarray_start: subarray_end])