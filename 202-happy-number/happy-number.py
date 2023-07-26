class Solution:
    def isHappy(self, n: int) -> bool:
        squared_sums = set() 
        while n not in squared_sums:
            squared_sums.add(n)
            
            updated_n = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                updated_n += digit
                n = n // 10

            n = updated_n

            if n == 1:
                return True

        return False
