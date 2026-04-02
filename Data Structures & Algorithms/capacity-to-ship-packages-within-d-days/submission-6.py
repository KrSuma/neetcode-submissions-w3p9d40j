class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        res = float('inf')

        def func(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while l <= r:
            m = (r + l) // 2

            if func(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
            
