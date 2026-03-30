class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        for n in nums:
            copy.append(n)
        return copy