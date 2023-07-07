class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #get length of nums list
        nums_length = len(nums)
        
        quadruplets = []

        #sort nums list, so we can skip duplicated numbers
        nums.sort() 

        for index_, val_ in enumerate(nums):
            #skip repeated numbers
            if index_ > 0 and val_ == nums[index_ - 1]:
                continue

            for index, val in enumerate(nums): 
                
                #use two ptrs solutions and assume it is a two sum problem 
                first_ptr, second_ptr = index + 1, nums_length - 1
                while first_ptr < second_ptr:
                    four_sum = val_ + val + nums[first_ptr] + nums[second_ptr]
                    if four_sum > target:
                        second_ptr = second_ptr - 1

                    elif four_sum < target:
                        first_ptr = first_ptr + 1

                    else:
                        quadruplet = [val_, val, nums[first_ptr], nums[second_ptr]]
                        quadruplet.sort()
                        if len(set([index_, index, first_ptr, second_ptr])) == 4 and quadruplet not in quadruplets:
                            quadruplets.append(quadruplet)
                        first_ptr = first_ptr + 1
                        while nums[first_ptr] == nums[first_ptr - 1] and first_ptr < second_ptr:
                            first_ptr = first_ptr + 1
        return quadruplets
