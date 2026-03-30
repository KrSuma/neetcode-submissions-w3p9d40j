class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)

        res = []
        for k, v in count.items():
            if v > int(len(nums) / 3):
                res.append(k)
        return res