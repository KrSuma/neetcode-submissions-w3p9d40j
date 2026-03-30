class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb, res = [], []

        def backtrack(i):
            if i > n:
                if len(comb) == k:
                    res.append(comb.copy())
                return
            
            comb.append(i)
            backtrack(i + 1)
            comb.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return res