class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        bucket = [[] for n in range(len(nums) + 1)]

        for key, v in count.items():
            bucket[v].append(key)

        res = []
        for i in (range(len(bucket)-1, -1, -1)):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return res