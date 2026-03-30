class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap, key = freq of all letters, value = list of strings

        hashmap = defaultdict(list)
        
        for s in strs:
            counter = [0] * 26
            for letter in s:
                counter[ord(letter)-ord('a')] += 1
            hashmap[tuple(counter)].append(s)
            
        return list(hashmap.values())