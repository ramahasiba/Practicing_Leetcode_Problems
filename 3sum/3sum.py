class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        triplets = []
        nums.sort()
        nums_length = len(nums)

        for index, val in enumerate(nums):
            #skip repeated numbers
            if index > 0 and val == nums[index - 1]:
                continue
            
            #use two ptrs solutions and assume it is a two sum problem 
            first_ptr, second_ptr = index + 1, nums_length - 1
            while first_ptr < second_ptr:
                three_sum = val + nums[first_ptr] + nums[second_ptr]
                if three_sum > 0:
                    second_ptr = second_ptr - 1

                elif three_sum < 0:
                    first_ptr = first_ptr + 1

                else:
                    triplets.append([val, nums[first_ptr], nums[second_ptr]])
                    first_ptr = first_ptr + 1
                    while nums[first_ptr] == nums[first_ptr - 1] and first_ptr < second_ptr:
                        first_ptr = first_ptr + 1
        return triplets