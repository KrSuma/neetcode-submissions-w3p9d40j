class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        CounterS = defaultdict(int)
        CounterT = defaultdict(int)

        for s, t in zip(s, t):
            CounterS[s] += 1
            CounterT[t] += 1
        
        return CounterS == CounterT
