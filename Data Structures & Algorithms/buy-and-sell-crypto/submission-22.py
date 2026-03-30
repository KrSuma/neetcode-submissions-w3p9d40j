class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        profit = 0

        for r in range(1, len(prices)):
            while prices[l] > prices[r]:
                l += 1
            else:
                diff = prices[r] - prices[l]
                profit = max(diff, profit)
        
        return profit