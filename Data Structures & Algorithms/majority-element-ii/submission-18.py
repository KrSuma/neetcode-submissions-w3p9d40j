class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1

            if len(hashmap) <= 2:
                continue
            
            temp = defaultdict(int)
            for k, v in hashmap.items():
                if v > 1:
                    temp[k] = v - 1
            hashmap = temp
        
        res = []
        for n in hashmap:
            if nums.count(n) > len(nums) / 3:
                res.append(n)
        
        return res