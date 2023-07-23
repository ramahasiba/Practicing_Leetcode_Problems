class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast_ptr, slow_ptr = 0, 0
        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
            if slow_ptr == fast_ptr:
                break

        sec_slow_ptr = 0
        while True:
            slow_ptr = nums[slow_ptr]
            sec_slow_ptr = nums[sec_slow_ptr]
            if slow_ptr == sec_slow_ptr:
                return sec_slow_ptr 