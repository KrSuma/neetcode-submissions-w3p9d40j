class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minlength = float('inf')
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minlength = min(minlength, r - l + 1)
                total -= nums[l]
                l += 1
            
        return 0 if minlength == float('inf') else minlength
        

