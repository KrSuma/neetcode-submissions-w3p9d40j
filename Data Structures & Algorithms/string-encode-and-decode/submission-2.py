class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            count = str(len(s))
            encoded += count + '#' + s
        return encoded 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find occurance of the first '#' after index i
            j = s.find('#', i)
            # extract length before '#'
            length = int(s[i:j])
            content = s[j + 1: j + 1 + length]
            res.append(content)
            i = j + 1 + length
        return res
            
                