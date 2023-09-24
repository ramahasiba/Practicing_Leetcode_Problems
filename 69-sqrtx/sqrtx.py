class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
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