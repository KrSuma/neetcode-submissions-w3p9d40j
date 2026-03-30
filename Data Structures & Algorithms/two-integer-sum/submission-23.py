class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    
        hash_map = {}
        res = []

        for i, n in enumerate(nums):
            if n in hash_map:
                res = [hash_map[n], i]
            else:
                diff = target - n
                hash_map[diff] = i
        return res