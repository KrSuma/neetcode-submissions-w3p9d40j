class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l, r = 0 , 1
        while l < len(nums)-1:
            while r < len(nums):
                if nums[l] == nums[r]:
                    return True
                r += 1
            l += 1
            r = l + 1
        return False 