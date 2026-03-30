class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        hashmap = defaultdict(int)
        l = 0 
        min_op = float('inf')

        for r in range(len(blocks)):

            hashmap[blocks[r]] += 1

            if r - l + 1 > k:
                hashmap[blocks[l]] -= 1
                l += 1
            if r - l + 1 == k:
                min_op = min(hashmap['W'], min_op)

        return min_op