class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_number = len(prices)
        min_price_index = 0
        min_price = prices[0]
        max_price_index = 1
        max_price = 0
        max_profit = 0 
        for index in range(2, prices_number + 1):
            searching_list = prices[index - 2: index]
            current_min_price = min(searching_list)
            current_max_price = max(searching_list)
            current_max_price_index = searching_list.index(current_max_price)
            if current_max_price_index == 1:
                if current_min_price < min_price:
                    min_price =  current_min_price
                    max_price = current_max_price
                if current_max_price > max_price:
                    max_price = current_max_price

                current_max_profit = max_price - min_price
                if current_max_profit > max_profit:
                    max_profit = current_max_profit

        if max_profit > 0:
            return max_profit
        else: 
            return 0 