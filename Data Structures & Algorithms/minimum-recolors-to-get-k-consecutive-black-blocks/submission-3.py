class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hashmap = defaultdict(int)
        l = 0
        res = float('inf')

        for r in range(len(blocks)):
            hashmap[blocks[r]] += 1
            
            while r - l + 1 > k:
                hashmap[blocks[l]] -= 1
                l += 1

            if r - l + 1 == k:
                res = min(res, hashmap['W'])
            
        
        return res