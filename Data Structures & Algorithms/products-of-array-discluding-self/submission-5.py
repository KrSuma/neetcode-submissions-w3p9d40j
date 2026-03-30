class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        j = 0
        for i in range(len(nums)):
            total = 1
            while j < len(nums):
                if j != i:
                    total *= nums[j]    
                j += 1
            res.append(total)
            j = 0
        return res