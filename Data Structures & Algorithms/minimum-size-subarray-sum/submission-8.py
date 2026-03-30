class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minLength = float('inf')
        total = 0

        while r < len(nums):
            total += nums[r]
            while total >= target:
                minLength = min(minLength, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        
        return 0 if minLength == float('inf') else minLength