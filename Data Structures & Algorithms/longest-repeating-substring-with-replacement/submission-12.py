class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        l = 0 
        length = 0

        for r in range(len(s)):
            count[s[r]] += 1

            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            length = max(r - l + 1, length)
        
        return length 
