class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for s in s:
            countS[s] += 1
        for t in t :
            countT[t] += 1
        
        return countS == countT