class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l, r = 0, 0
        res = 0
        total = 0

        while r < len(arr):
            
            if r - l + 1 > k:
                total -= arr[l]
                l += 1

            total += arr[r]
            
            if r - l + 1 == k and int(total / (r - l + 1)) >= threshold:
                res += 1

            r += 1
        
        return res
