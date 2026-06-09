class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i, j in zip(s, t):
            countS[i] += 1
            countT[j] += 1
        
        if len(s) != len(t):
            return False
        
        return countS == countT