class Solution:
    def twoSum(self, nums, target: int): 
        for index, number in enumerate(nums): 
            remainder = target - number 
            if remainder in nums[index + 1: ]:
                remainder_index  = nums[index + 1: ].index(remainder) 
                return [index, remainder_index + index + 1] 