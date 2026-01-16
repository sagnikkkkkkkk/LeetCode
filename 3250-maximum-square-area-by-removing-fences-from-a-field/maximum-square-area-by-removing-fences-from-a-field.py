class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        MOD = 10**9 + 7

        h = sorted(hFences + [1 , m])
        v = sorted(vFences + [1 , n])

        hg = set()
        for i in range(len(h)):
            for j in range(i+1 , len(h)):
                hg.add(h[j] - h[i])

        vg = set()
        for i in range(len(v)):
            for j in range(i+1 , len(v)):
                vg.add(v[j] - v[i])

        c = hg & vg
        if not c:
            return -1
        
        s = max(c)
        return (s * s) % MOD