class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = [[] for x in range(len(nums) + 1)]
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        for n, c in freq.items():
            count[c].append(n)
        
        res = []
        for i in range(len(count)-1, -1, -1):
            for n in count[i]:
                if len(res) == k:
                    return res
                res.append(n)
        return res