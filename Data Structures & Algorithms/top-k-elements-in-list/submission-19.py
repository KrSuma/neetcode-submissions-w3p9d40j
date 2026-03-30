class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for x in range(len(nums) + 1)]
        count = defaultdict(int)
        res = []

        for n in nums:
            count[n] += 1
        
        for key, val in count.items():
            bucket[val].append(key)
        
        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                if len(res) == k:
                    return res
                res.append(n)

        return res