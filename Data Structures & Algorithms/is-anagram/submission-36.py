class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        if len(s) != len(t):
            return False

        for s, t in zip(s, t):
            countS[s] += 1
            countT[t] += 1
        
        return countS == countT