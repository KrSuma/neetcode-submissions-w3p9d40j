class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        res = ''

        for p in path + '/':
            if p != '/':
                res += p
            else:
                if res == '..':
                    if stack:
                        stack.pop()
                elif res != '.' and res != '':
                    stack.append(res)
                res = ''
        
        return '/' + '/'.join(stack)