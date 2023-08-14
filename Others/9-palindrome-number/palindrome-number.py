class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # else:
        x = str(x)
        x_length = len(x)

        l, r = 0, x_length - 1
        while l <= r:
            if x[l] == x[r]:
                r -= 1
                l += 1
            else:
                return False
        return True