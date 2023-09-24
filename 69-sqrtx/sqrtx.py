class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        else:
            a, b, ans = 0, x, 0
            while abs(a - b) != 1:
                mid = (a + b) // 2
                if mid * mid == x:
                    return mid
                if mid * mid > x:
                    b = mid
                else:
                    a = mid
                    ans = a
            return a

            # counter = 2
            # while counter * counter <= x:
            #     counter += 1
            # return counter - 1


        