class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        minlength = min(len(word1), len(word2))
        for i in range(minlength):
            res.append(word1[i])
            res.append(word2[i])
        
        res.append(word1[minlength:])
        res.append(word2[minlength:])

        return ''.join(res)