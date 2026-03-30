class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = defaultdict(int)

        maxval = 0
        res = [0, 0]

        for n in nums:
            count[n] += 1
        for n, cnt in count.items():
            if maxval < cnt:
                res[0], res[1] = n, cnt
                maxval = cnt
            
        return res[0]