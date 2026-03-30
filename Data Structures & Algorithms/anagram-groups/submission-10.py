class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = count of all the letters 
        # val = list of strings

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter)-ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())