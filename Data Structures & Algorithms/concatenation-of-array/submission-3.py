class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        to_copy = nums.copy()
        for n in nums:
            to_copy.append(n)
        return to_copy