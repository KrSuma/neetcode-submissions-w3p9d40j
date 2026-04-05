class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []

        length = min(len(word1), len(word2))
        for i in range(length):
            res.append(word1[i])
            res.append(word2[i])
        
        res.append(word1[length:])
        res.append(word2[length:])

        return ''.join(res)