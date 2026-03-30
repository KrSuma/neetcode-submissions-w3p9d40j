class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = [[] for i in range(len(nums) + 1)]

        hashmap = Counter(nums)
        for num, val in hashmap.items():
            count[val].append(num)
        
        res = []
        for i in range(len(count)-1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res