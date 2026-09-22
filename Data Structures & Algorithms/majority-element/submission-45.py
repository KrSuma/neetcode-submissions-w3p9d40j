class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            if c > len(nums) // 2:
                return n
        
        