class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = [[] for x in range(len(nums) + 1)]
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        for num, freq in hashmap.items():
            count[freq].append(num)
        
        res = []
        for i in range(len(count)-1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res