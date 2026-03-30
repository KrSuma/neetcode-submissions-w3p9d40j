class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = (r + l) // 2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / m)
            if total > h:
                l = m + 1
            else:
                r = m - 1
        return l
