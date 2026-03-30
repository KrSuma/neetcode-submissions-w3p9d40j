class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        to_copy = nums.copy()
        for n in to_copy:
            nums.append(n)
        return nums