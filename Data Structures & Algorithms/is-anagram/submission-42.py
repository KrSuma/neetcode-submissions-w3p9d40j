class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i, j in zip(s, t):
            countS[i] += 1
            countT[j] += 1
        
        return countS == countT