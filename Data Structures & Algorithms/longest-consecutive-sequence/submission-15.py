class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)

        res = float('-inf')

        for n in nums:
            if n - 1 not in hashset:
                length = 0
                while n + length in hashset:
                    length += 1
                res = max(res, length)
        
        return 0 if res == float('-inf') else res