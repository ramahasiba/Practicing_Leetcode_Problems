class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_len = len(arr)
        ans = 0
        for index in range(arr_len):
            #element multiplied by its frequency in odd sub-arrays.
            ans += ((index + 1) * (arr_len - index) + 1) // 2 * arr[index] 
        return ans
