class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ''

        for i in range(len(strs[0])):
            for c in strs:
                if len(c) - 1 < i or strs[0][i] != c[i]:
                    return res 
            res += strs[0][i]
        
        return res