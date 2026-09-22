class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        CountS = defaultdict(int)
        CountT = defaultdict(int)

        for c in s:
            CountS[c] += 1
        for c in t:
            CountT[c] += 1
        
        if len(s) != len(t):
            return False
        
        return CountS == CountT