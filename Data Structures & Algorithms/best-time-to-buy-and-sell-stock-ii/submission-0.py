class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0

        while j < len(prices):
            if prices[i] > prices[j]:
                i += 1
                j += 1
            else:
                diff = prices[j] - prices[i]
                profit += diff
                i = j
                j = i +1
        
        return profit
            