class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)): # build the prefix
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1): # build the suffix
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        