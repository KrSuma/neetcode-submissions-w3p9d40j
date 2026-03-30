class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                diff = prices[r] - prices[l]
                profit = max(profit, diff)
        return profit
            
