class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashset = defaultdict(int)

        res = 0
        maxCount = 0

        for n in nums:
            hashset[n] += 1
            if maxCount < hashset[n]:
                res = n
                maxCount = hashset[n]
        return res