class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        length = min(len(word1), len(word2))
        i = 0

        while i < length:
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        
        if len(word1) > len(word2):
            res.append(word1[length:])
        else:
            res.append(word2[length:])
        
        return ''.join(res)
