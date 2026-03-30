from collections import heapq, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         
        # {1:1, 2:2, 3:3}
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        
        # [[1,1],[2,2],[3,3]] 
        res = []
        for n, cnt in dic.items():
            res.append([cnt, n])
        
        res.sort()
        
        # [3, 2]
        ret = []
        while len(ret) < k:
            ret.append(res.pop()[1])
        return ret