class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heaviest = [-x for x in stones]
        heapq.heapify(heaviest)

        while len(heaviest) >= 2:
            first = -heapq.heappop(heaviest)
            second = -heapq.heappop(heaviest)
            if second < first:
                newweight = first - second
                heapq.heappush(heaviest, -newweight)

        return 0 if not heaviest else -heaviest[0] 