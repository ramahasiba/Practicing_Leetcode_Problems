class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dictionary = {}
        for num in nums:
            if num in nums_dictionary:
                nums_dictionary[num] = nums_dictionary[num] + 1
            else:
                nums_dictionary[num] = 1 
                
        for key in nums_dictionary: 
            if nums_dictionary[key] == 1:
                return key
            else:
                continue


