class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def mc(a):
            a.sort()
            l = c = 1

            for i in range(1 , len(a)):
                if a[i] == a[i - 1] + 1:
                    c += 1 
                else:
                    c = 1
                l = max(l , c)

            return l + 1

        mh = mc(hBars)
        mv = mc(vBars)

        s = min(mh , mv)
        return s*s