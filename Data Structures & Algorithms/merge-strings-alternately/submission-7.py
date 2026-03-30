class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1_length = len(word1)
        word2_length = len(word2)
        length = min(word1_length, word2_length)

        res = ''
        for i in range(length):
            res += word1[i]
            res += word2[i]
        
        if word1_length > word2_length:
            res += word1[word2_length:]
        else:
            res += word2[word1_length:]
        return res

