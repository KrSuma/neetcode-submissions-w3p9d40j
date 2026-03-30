class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curset, subset = [], []
        
        def backtrack(i):
            if i == len(nums):
                subset.append(curset.copy())
                return 

            # include nums[i]
            curset.append(nums[i])
            backtrack(i + 1)
            curset.pop()
            # dont include nums[i]
            backtrack(i + 1)
        
        backtrack(0)
        return subset