class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # speed = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile/speed)
            
        #     if totalTime <= h:
        #         return speed
            
        #     speed += 1
        # return speed

        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (r + l) // 2
            
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / k) 
            
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
