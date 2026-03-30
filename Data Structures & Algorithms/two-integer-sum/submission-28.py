class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hasing 
        hash_set = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_set:
                return [hash_set[diff], i]
            hash_set[n] = i

        return []