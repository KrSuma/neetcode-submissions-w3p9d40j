class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # key = freq of chars, value = list of strs
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter)-ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())