class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        res = []

        for i, n in enumerate(nums):
            if n in hashmap:
                res = [hashmap[n], i]
            else: 
                diff = target - n
                hashmap[diff] = i

        return res