class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if len(count) > 2:
                temp = defaultdict(int)
                for num, c in count.items():
                    if c > 1:
                        temp[num] = c - 1
                count = temp
        
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res