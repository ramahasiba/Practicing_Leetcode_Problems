class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_len = len(arr) 
        summation, counter = 0, 1 
        while counter <= arr_len and counter % 2 == 1:
            for index in range(arr_len): 
                if counter + index <= arr_len:
                    summation += sum(arr[index: counter + index])
            counter += 2 
        return summation