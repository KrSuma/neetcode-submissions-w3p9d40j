class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = maxCount = 0
        for c in counter:
            if counter[c] > maxCount:
                res = c
                maxCount = counter[c]
        return res

        # count = defaultdict(int)
        # res = maxCount = 0

        # for n in nums:
        #     count[n] += 1
        #     if maxCount < count[n]:
        #         res = n
        #         maxCount = count[n]
        # return res