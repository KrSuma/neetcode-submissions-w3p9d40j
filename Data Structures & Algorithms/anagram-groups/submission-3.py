class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sort = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            sort[sortedS].append(s)
        return sort.values()
