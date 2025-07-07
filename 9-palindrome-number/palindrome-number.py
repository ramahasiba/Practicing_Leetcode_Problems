class Solution:
    def isPalindrome(self, x: int) -> bool: 
        # x = str(x)
        # x_length = len(x)

        # l, r = 0, x_length - 1
        # while l <= r:
        #     if x[l] == x[r]:
        #         r -= 1
        #         l += 1
        #     else:
        #         return False
        # return True

        str_num = str(x)
        num_len = len(str_num)
        r, l = 0, num_len - 1
        while r < l:
            if str_num[r] == str_num[l]:
                r+=1
                l-=1
            else: 
                return False
        return True