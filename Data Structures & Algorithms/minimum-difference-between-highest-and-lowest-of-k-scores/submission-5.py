class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        min_diff = float('inf')

        l = 0
        for r in range(k - 1, len(nums)):
            if r - l + 1 > k:
                l += 1
            
            diff = nums[r] - nums[l]
            min_diff = min(min_diff, diff)
        return min_diff if min_diff != float('inf') else 0