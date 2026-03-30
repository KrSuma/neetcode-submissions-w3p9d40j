class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''

        min_length = min(len(word1), len(word2)) 
        for i in range(min_length):
            res += word1[i]
            res += word2[i]
        
        if len(word1) > min_length:
            res += word1[i+1:]
        if len(word2) > min_length:
            res += word2[i+1:]
        
        return res