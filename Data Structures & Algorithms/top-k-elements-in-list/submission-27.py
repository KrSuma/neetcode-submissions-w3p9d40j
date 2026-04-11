class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = [[] for x in range(len(nums) + 1)]
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        for num, cnt in freq.items():
            count[cnt].append(num)

        res = []
        for i in range(len(count)-1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
        