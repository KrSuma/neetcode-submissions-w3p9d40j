class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_table = {}

        for i, n in enumerate(nums):
            if n not in hash_table:
                diff = target - n
                hash_table[diff] = i
            else:
                return [hash_table[n], i]
        return []