class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        if len(max_heap) < 2:
            return -max_heap[0]

        while max_heap and len(max_heap) >= 2:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x != y:
                new_stone = y - x
                heapq.heappush(max_heap, -new_stone)
                
        return 0 if not max_heap else -max_heap[0]
