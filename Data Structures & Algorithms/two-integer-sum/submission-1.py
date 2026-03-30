class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while l < len(nums)-1:
            while r < len(nums):
                if nums[l] + nums[r] == target:
                    return [l, r]
                r += 1
            l += 1
            r = l + 1
            