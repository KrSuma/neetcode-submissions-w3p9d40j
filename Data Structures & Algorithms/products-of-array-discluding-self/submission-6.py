class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # res = []
        # j = 0
        # for i in range(len(nums)):
        #     total = 1
        #     while j < len(nums):
        #         if j != i:
        #             total *= nums[j]    
        #         j += 1
        #     res.append(total)
        #     j = 0
        # return res

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res