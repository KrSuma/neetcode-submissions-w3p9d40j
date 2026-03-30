class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1

            if len(hashmap) <= 2:
                continue
            
            temp = defaultdict(int)
            for num, c in hashmap.items():
                if c > 1:
                    temp[num] = c - 1
            hashmap = temp

        res = []
        for n in hashmap:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res
