class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority = [0, 0]
        for c in counter:
            if counter[c] > majority[1]:
                majority[0] = c
                majority[1] = counter[c]
        return majority[0]