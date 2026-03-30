class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0 
        res = 0 
        current_sum = sum(arr[:k-1])

        def average(total, k):
            return total / k

        for r in range(k - 1, len(arr)):
            current_sum += arr[r]
            
            if r - l + 1 > k:
                current_sum -= arr[l]
                l += 1
            
            if average(current_sum, k) >= threshold:
                res += 1
        
        return res