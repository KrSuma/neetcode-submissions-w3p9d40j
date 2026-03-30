class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # counter = Counter(nums)
        # res = [item[0] for item in counter.most_common(k)]
        # return res

        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        