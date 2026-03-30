class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        res, key = 0, 0
        for k, v in counter.items():
            if res < v:
                res = max(v, res)
                key = k
        return key