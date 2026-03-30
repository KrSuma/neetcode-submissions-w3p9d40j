class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        i = 0
        res = []
        while i < len(nums):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product *= nums[j]
            res.append(product)
            i += 1
        return res
        