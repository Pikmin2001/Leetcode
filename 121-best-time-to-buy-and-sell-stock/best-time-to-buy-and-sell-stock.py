class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]

        for price in prices[1:]:
            profit = price - buyPrice
            maxProfit = max(profit, maxProfit)
            buyPrice = min(buyPrice, price)
        return maxProfit
        