class Solution:
    def twoSum(self, nums, target: int):  
        for index, num in enumerate(nums):
            for index_2, num_2 in enumerate(nums[index+1:]):
                if num + num_2 == target:
                    print(num, num_2)
                    return [index, index_2 + index + 1]    