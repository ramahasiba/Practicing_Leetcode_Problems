import numpy as np
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        original_array = np.array(nums)
        absolute_values = np.abs(original_array)
        absolute_values.sort()
        absolute_squares = np.square(absolute_values)
        return absolute_squares

