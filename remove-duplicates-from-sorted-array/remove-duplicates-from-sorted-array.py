class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:   
        list_len = len(nums)
        counter = 0
        # if list_len == 2:
        #     if nums[0] == nums[1]: 
        #         return 1
        #     else: 
        #         return 2
        # else:
        for index in range(list_len - 1) : 
            if nums[index - counter] == nums[index + 1 - counter]:
                counter = counter + 1
                nums[index + 1 - counter:] = nums[index + 2 - counter:] 
        unique_length = len(nums)
        return unique_length