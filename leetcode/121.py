class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if len(prices) < 2:
            return max_profit

        min_num = prices[0]

        for num in prices[1:]:
            min_num = min(num, min_num)
            max_profit = max(max_profit, num - min_num)

        return max_profit
