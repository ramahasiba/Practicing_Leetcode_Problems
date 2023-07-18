class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        #get nums length 
        nums_length = len(nums)

        #check if there is numbers
        if nums_length == 0:
            return 0
        elif nums_length == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0
         
        first_ptr = 0

        sub_array_summation = 0

        min_sub_array_length = float('inf')

        for sec_ptr in range(nums_length):
            sub_array_summation += nums[sec_ptr]
        
            while sub_array_summation >= target:
                if (sec_ptr - first_ptr + 1) < min_sub_array_length:
                    min_sub_array_length = sec_ptr - first_ptr + 1
                
                sub_array_summation -= nums[first_ptr]

                first_ptr += 1
        
        if min_sub_array_length == float('inf'):
            return 0
        
        return min_sub_array_length