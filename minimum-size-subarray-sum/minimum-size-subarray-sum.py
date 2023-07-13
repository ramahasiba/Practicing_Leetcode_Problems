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
        
        #sort the list
        # nums.sort()
   
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



        # sub_array = []

        # while first_ptr < sec_ptr:
        #     two_sum = filtered_nums[first_ptr] + filtered_nums[sec_ptr]

        #     if two_sum > target:
        #         sec_ptr -= 1
        #     elif two_sum == target:
        #         return 2
        #     else:
        #         first_ptr += 1

        # #initiate length_counter to prevent looping the array more than number of numbers
        # length_counter = filtered_nums_length - 2 ء

        # while sub_array_length <= filtered_nums_length - 2 and  length_counter >= 0:
        #     for num in filtered_nums:
        #         if (num + sub_array_sum) < target and sub_array_sum < (num + sub_array_sum):
        #             sub_array_sum = num + sub_array_sum
        #             sub_array_length += 1

        #         elif num + sub_array_sum >= target:
        #             return sub_array_length + 1

        #     length_counter -= 1
        
        # return 0
            

