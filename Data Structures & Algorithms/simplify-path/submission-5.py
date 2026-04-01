class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        res = ''

        for c in path + '/':
            if c == '/':
                if res == '..':
                    if stack: stack.pop()
                elif res != '.' and res != '':
                    stack.append(res)
                res = ''
            else:
                res += c

        return '/' + '/'.join(stack)