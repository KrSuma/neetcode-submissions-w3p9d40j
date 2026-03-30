class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        max_val = 0 
        res = 0

        for k, v in counter.items():
            if v > max_val:
                max_val = max(max_val, v)
                res = k
        return res
