class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1 + 2 <-> 1 2 + 
        # stack = [1,2,+] 
        # if + is popped, take 2 our then calculate, then put back the result

        stack = []

        for t in tokens:
            if t == '+':
                if stack:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(first + second)
            elif t == '-':
                if stack:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second - first)
            elif t == '*':
                if stack:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(first * second)
            elif t == '/':
                if stack:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(second / first))
            else:
                stack.append(int(t))
            
        return stack[0]