class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        else:
            counter = 2
            while counter * counter <= x:
                counter += 1
            return counter - 1


        