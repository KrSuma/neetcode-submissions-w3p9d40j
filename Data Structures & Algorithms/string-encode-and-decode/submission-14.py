class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            string = s[r + 1 : r + 1 + length]
            res.append(string)
            r = r + 1 + length
            l = r
        
        return res
