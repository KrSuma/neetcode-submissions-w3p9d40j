class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap where key = difference of target - n, value = index 
        
        hashmap = {}
        for i, n in enumerate(nums):
            if n in hashmap:
                return [hashmap[n], i]
            else:
                diff = target - n
                hashmap[diff] = i
        return []