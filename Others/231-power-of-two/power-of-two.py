class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        float_ans = math.log2(n)
        if float_ans == int(float_ans):
            return True
        else: 
            return False