class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashing = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashing:
                return [hashing[diff], i]
            hashing[n] = i
        return []