class Solution:
    def sum_squares(self, n):         
        updated_n = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            updated_n += digit
            n = n // 10

        n = updated_n 

        return n
        
    def isHappy(self, n: int) -> bool: 
        slow = self.sum_squares(n)
        fast = self.sum_squares(self.sum_squares(n))

        while slow!=fast and fast!=1:
            slow = self.sum_squares(slow)
            fast = self.sum_squares(self.sum_squares(fast))
            
        return fast==1   