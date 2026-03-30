class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                new_stone = first - second
                heapq.heappush(stones, -new_stone)
        
        return 0 if not stones else -stones[0]