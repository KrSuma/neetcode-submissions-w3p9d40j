class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashtable = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashtable:
                return [hashtable[diff], i]
            hashtable[n] = i

        return [] 
        
