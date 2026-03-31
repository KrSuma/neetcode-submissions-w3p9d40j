class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0 
        minlength = float('inf')
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minlength = min(r - l + 1, minlength)
                total -= nums[l]
                l += 1
        
        return 0 if minlength == float('inf') else minlength

