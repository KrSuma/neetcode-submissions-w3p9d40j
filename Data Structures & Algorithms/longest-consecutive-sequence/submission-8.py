class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)

        res = 0 

        for n in nums:
            length = 1
            if n - 1 not in hashset:
                while n + length in hashset:
                    length += 1
            res = max(res, length)

        return res 
