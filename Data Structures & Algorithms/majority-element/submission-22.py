class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # count, res = 0, 0

        # for n in nums:
        #     if count == 0:
        #         res = n
        #     count += (1 if res == n else -1)

        # return res

        # dict

        count = Counter(nums)
        maxval, res = 0, 0
        for num, cnt in count.items():
            if maxval < cnt:
                maxval = cnt
                res = num
        return res