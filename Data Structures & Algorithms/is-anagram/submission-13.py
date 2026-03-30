from collections import Counter, defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        
        for letter in s:
            if letter in map_s:
                map_s[letter] += 1
            else:
                map_s[letter] = 1
        
        for letter in t:
            if letter in map_t:
                map_t[letter] += 1
            else:
                map_t[letter] = 1
        
        return map_s == map_t