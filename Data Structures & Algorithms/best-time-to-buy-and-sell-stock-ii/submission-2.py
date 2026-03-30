class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        j = 0

        total = 0
        for i in range(1, len(prices)):
            if prices[j] >= prices[i]:
                j += 1
            else:
                diff = prices[i] - prices[j]
                total += diff
                j += 1
        
        return total