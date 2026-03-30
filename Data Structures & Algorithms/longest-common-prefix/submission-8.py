class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: # if index goes out of bounds of the first word
                    return res
            res += strs[0][i]
        return res