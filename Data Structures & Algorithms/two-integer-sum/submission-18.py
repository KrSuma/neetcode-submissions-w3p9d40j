class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        answer = []

        # key = difference, value = index
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in diffs:
                diffs[n] = i
            else:
                return [diffs[diff], i]
        
        



