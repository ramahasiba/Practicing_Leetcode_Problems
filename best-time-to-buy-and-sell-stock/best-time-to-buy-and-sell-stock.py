class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        first_ptr, sec_ptr = 0, 1
        max_profit = 0

        number_of_prices = len(prices)
        while sec_ptr < number_of_prices:
            #check if the these two items profitable
            if prices[first_ptr] < prices[sec_ptr]:
                profit = prices[sec_ptr] - prices[first_ptr]
                max_profit = max(max_profit, profit)
            else:
                first_ptr = sec_ptr
            sec_ptr = sec_ptr + 1

        return max_profit