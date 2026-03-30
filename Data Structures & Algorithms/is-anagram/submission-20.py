class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = defaultdict(int)
        dictT = defaultdict(int)

        for l in s:
            dictS[l] += 1
        for l in t:
            dictT[l] += 1
        
        return dictS == dictT