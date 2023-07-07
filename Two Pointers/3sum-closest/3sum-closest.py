import numpy as np
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 92233720368547
        nums_length = len(nums)
        result_ = sum(nums[: 3])
        nums.sort() 
        for index, val in enumerate(nums):
            #skip repeated numbers
            if index > 0 and val == nums[index - 1]:
                continue
            
            #use two ptrs solutions and assume it is a two sum problem 
            first_ptr, second_ptr = index + 1, nums_length - 1
            while first_ptr < second_ptr:
                three_sum = val + nums[first_ptr] + nums[second_ptr]
                curent_diff = np.abs(target - three_sum)

                if curent_diff < diff:
                    result_ = three_sum
                    diff = curent_diff

                if three_sum > target:
                    second_ptr = second_ptr - 1

                elif three_sum < target:
                    first_ptr = first_ptr + 1

                else:
                    return three_sum
        return result_