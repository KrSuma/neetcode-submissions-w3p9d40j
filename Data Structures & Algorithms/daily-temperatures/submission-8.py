class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 for x in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackIndx = stack.pop()
                res[stackIndx] = i - stackIndx
            stack.append([t, i])
        
        return res