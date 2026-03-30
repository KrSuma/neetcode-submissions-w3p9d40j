class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                diff = prices[r] - prices[l]
                res = max(diff, res)
            r += 1
        return res