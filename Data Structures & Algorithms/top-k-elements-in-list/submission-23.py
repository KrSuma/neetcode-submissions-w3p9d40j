class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)
        freq = [[] for x in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] += 1
        
        for key, val in hashmap.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)
        
        return res