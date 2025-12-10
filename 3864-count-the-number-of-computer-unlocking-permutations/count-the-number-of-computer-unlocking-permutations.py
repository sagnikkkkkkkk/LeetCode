class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        Mod = 10**9 + 7
        n = len(complexity)
        for i in range(1 , n) :
            if complexity[i] <= complexity[0] :
                return 0

        res = 1
        for k in range(1 , n) :
            res = (res * k) % Mod
        return res