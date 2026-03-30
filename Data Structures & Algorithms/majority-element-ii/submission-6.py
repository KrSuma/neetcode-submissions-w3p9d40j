class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            
            if len(count) <= 2:
                continue
            
            temp = defaultdict(int)
            for num, cnt in count.items():
                if cnt > 1:
                    temp[num] = cnt - 1
            count = temp
        
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res