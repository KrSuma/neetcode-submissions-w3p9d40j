class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in s:
            countS[i] += 1
        
        for i in t:
            countT[i] += 1

        return countS == countT