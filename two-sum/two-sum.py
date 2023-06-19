class Solution:
    def twoSum(self, nums, target: int):  
        list_length = len(nums)
        if list_length == 2:
            return [0, 1]    
        sorted_nums = nums.copy()
        sorted_nums.sort() 
        first_ptr_index = 0    
        second_ptr_index = list_length - 1
        while first_ptr_index < second_ptr_index:
            #check if the sum of numbers at the first and second index is greater than the target number then reduce the second_ptr_index by 1, if it is less than the target one then add 1 to the first_ptr_index.
            first_number = sorted_nums[first_ptr_index]
            second_number = sorted_nums[second_ptr_index]
            summation_ = first_number +  second_number
            if summation_ == target:  
                if first_number == second_number:
                    first_ptr_index = nums.index(sorted_nums[first_ptr_index])
                    second_ptr_index = nums[first_ptr_index + 1:].index(second_number)
                    return [first_ptr_index, (second_ptr_index + first_ptr_index + 1)]
        
                else:
                    first_ptr_index = nums.index(sorted_nums[first_ptr_index])
                    second_ptr_index = nums.index(sorted_nums[second_ptr_index])
                    return [first_ptr_index, second_ptr_index]

            elif summation_ > target:
                second_ptr_index = second_ptr_index - 1
            else: 
                first_ptr_index = first_ptr_index + 1