class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False

        for s in s:
            countS[s] = 1 + countS.get(s, 0)
        for t in t:
            countT[t] = 1 + countT.get(t, 0)
        
        return countS == countT