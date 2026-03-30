class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        count = Counter(nums)
        for key, val in count.items():
            bucket[val].append(key)
        
        for i in range(len(bucket)- 1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res
