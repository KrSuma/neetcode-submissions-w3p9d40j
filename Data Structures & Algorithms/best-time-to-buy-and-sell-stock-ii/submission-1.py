class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        j = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[j] >= prices[i]:
                j += 1
            else:
                diff = prices[i] - prices[j]
                profit += diff
                j += 1
        return profit    