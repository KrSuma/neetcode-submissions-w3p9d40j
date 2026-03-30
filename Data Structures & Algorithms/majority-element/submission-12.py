class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # use a hashmap, and for each n in nums, we add it to the hashmap: key = n, val = frequency
        # return the key with the most value (frequency)

        max_val = 0
        res = 0
        counter = Counter(nums)
        
        for k, v in counter.items():
            if v > max_val:
                res = k
            max_val = max(max_val, v)

        return res    
