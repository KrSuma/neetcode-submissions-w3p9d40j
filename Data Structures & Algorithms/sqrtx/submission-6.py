class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x - 1

        if x < 2:
            return x

        while l <= r:
            m = (r + l) // 2
            power = m ** 2
            
            if power > x:
                r = m - 1
            elif power < x:
                l = m + 1
            else:
                return m
        return r