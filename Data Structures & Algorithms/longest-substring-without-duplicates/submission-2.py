class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        setS = set()
        L = 0
        length = 0

        for R in range(len(s)):
            if s[R] in setS:
                while s[R] in setS:
                    setS.remove(s[L])
                    L += 1
            setS.add(s[R])
            length = max(R - L + 1, length)
        return length
        