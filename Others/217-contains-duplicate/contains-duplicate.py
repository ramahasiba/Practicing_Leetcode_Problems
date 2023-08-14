class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sort the list
        nums.sort()

        #get nums length 
        nums_length = len(nums)

        #iterate the list and check if there are equivalent contiguous numbers 
        for index in range(nums_length - 1):
            if nums[index] == nums[index + 1]:
                return True
            
        return False
