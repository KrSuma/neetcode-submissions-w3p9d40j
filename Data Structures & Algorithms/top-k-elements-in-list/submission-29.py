class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # bucket
        count = [[] for x in range(len(nums) + 1)]
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        for num, cnt in hashmap.items():
            count[cnt].append(num)
        
        res = []
        for i in range(len(count)-1, -1, -1):
            for n in count[i]:
                if len(res) == k:
                    return res
                res.append(n)
        
        return res