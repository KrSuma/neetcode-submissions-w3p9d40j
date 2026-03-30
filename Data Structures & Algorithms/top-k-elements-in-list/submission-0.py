class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we count the occurances of nums and add it in our dict
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # then for each num-freq pair, we swap to freq-num and sort it to ascending order
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        # we then pop the res k times to get k most elements
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

