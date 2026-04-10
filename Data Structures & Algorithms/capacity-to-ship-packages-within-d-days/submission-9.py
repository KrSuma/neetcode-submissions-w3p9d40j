class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        res = sum(weights)

        while l <= r:
            m = (r + l) // 2
            
            ships = 1
            cap = m
            for w in weights:
                if cap - w < 0:
                    ships += 1
                    cap = m
                cap -= w
            
            if ships <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
