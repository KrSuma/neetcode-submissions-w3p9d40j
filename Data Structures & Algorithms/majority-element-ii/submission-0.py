class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = Counter(nums)
        res = []

        for k, v in counter.items():
            if v > (len(nums) / 3):
                res.append(k)
        
        return res