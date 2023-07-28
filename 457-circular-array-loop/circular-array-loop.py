class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        nums_length = len(nums)
        checked = set()

        for index in range(nums_length):
            if index not in checked:
                cycle_set = set()
                while True:
                    if index in cycle_set:
                        return True
                    checked.add(index)
                    cycle_set.add(index)
                    prev, index = index, (index + nums[index]) % nums_length
                    if prev == index:
                        #unicycle
                        break
                    
                    if nums[prev] > 0 != nums[index] < 0:
                        break
        return False
