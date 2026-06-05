class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for n in s:
            countS[n] += 1
        for n in t:
            countT[n] += 1

        if len(countS) != len(countT):
            return False
        
        return countS == countT
        