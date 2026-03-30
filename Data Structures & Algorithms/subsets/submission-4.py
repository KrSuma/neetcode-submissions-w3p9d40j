class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curset, subset = [], []
        
        def dfs(i):
            if i == len(nums):
                subset.append(curset.copy())
                return
            
            # include
            curset.append(nums[i])
            dfs(i + 1)
            curset.pop()
            dfs(i + 1)
        
        dfs(0)
        return subset