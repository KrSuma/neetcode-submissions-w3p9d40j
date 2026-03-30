class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i, j = 0, 1

        profit = 0

        while j < len(prices):
            if prices[i] >= prices[j]:
                j += 1
            else:
                diff = prices[j] - prices[i]
                profit += diff
                j += 1
            i += 1
        
        return profit 