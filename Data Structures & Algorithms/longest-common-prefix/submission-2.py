class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_string = strs[0]
        result = ""
        
        for i, char in enumerate(first_string):
            counter = 0
            for string in strs:
                 if i < len(string) and char == string[i]:
                    counter += 1
            if counter == len(strs):
                result += char
            else:
                break
        
        return result