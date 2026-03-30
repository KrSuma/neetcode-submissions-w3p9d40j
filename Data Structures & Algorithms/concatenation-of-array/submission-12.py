class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        first = nums.copy()
        for n in nums:
            first.append(n)
        return first