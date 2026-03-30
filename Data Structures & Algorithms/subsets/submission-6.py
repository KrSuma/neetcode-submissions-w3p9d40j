class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i, nums, curset, subset):
            if i == len(nums):
                subset.append(curset.copy())
                return 

            # include nums[i]
            curset.append(nums[i])
            helper(i + 1, nums, curset, subset)
            curset.pop()
        
            # exclude nums[i]
            helper(i + 1, nums, curset, subset)

        curset, subset = [], []
        helper(0, nums, curset, subset)
        return subset


        
