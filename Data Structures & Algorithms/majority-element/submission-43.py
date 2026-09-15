class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ret = defaultdict(int)

        for n in nums:
            ret[n] += 1
        
        for i, n in ret.items():
            if n > len(nums) // 2:
                return i 
        