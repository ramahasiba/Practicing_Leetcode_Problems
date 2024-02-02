class Solution:
    def twoSum(self, nums, target: int):  
        #initiate nums_dict keys: target - num, and the value is num index
        nums_dict = {}
        for index, num in enumerate(nums):
            if num in nums_dict:
                return nums_dict[num], index
            else:
                nums_dict[target-num] = index