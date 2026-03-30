class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        l = 0 
        min_diff = float('inf')

        for r in range(k - 1, len(nums)):
            while r - l + 1 > k:
                l += 1
            
            diff = nums[r] - nums[l]
            min_diff = min(diff, min_diff)
        
        return min_diff if min_diff != float('inf') else 0