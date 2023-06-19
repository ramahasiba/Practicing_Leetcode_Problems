def counting_sort(arr):
    # Find the minimum and maximum values in the input list
    min_val = min(arr)
    max_val = max(arr)

    # Compute the range of values and create a count array
    count_range = max_val - min_val + 1
    count = [0] * count_range

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num - min_val] += 1

    # Create a sorted output array
    sorted_arr = []
    
    # Place the elements in their correct positions in the sorted array
    for i in range(count_range):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


class Solution:
    def twoSum(self, nums, target: int): 
        for index, number in enumerate(nums): 
            remainder = target - number 
            if remainder in nums[index + 1: ]:
                remainder_index  = nums[index + 1: ].index(remainder) 
                return [index, remainder_index + index + 1]
        # list_length = len(nums)
        # if list_length == 2:
        #     return [0, 1]    
        # sorted_nums = counting_sort(nums) 
        # first_ptr_index = 0    
        # second_ptr_index = list_length - 1
        # while first_ptr_index < second_ptr_index:
        #     #check if the sum of numbers at the first and second index is greater than the target number then reduce the second_ptr_index by 1, if it is less than the target one then add 1 to the first_ptr_index.
        #     first_number = sorted_nums[first_ptr_index]
        #     second_number = sorted_nums[second_ptr_index]
        #     summation_ = first_number +  second_number
        #     if summation_ == target:  
        #         if first_number == second_number:
        #             first_ptr_index = nums.index(sorted_nums[first_ptr_index])
        #             second_ptr_index = nums[first_ptr_index + 1:].index(second_number)
        #             return [first_ptr_index, (second_ptr_index + first_ptr_index + 1)]
        
        #         else:
        #             first_ptr_index = nums.index(sorted_nums[first_ptr_index])
        #             second_ptr_index = nums.index(sorted_nums[second_ptr_index])
        #             return [first_ptr_index, second_ptr_index]

        #     elif summation_ > target:
        #         second_ptr_index = second_ptr_index - 1
        #     else: 
        #         first_ptr_index = first_ptr_index + 1