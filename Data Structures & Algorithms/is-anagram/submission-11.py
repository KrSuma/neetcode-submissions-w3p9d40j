from collections import Counter, defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = defaultdict(int)
        map_t = defaultdict(int)
        
        for letter in s:
            map_s[letter] += 1
        for letter in t:
            map_t[letter] += 1
        
        return map_s == map_t