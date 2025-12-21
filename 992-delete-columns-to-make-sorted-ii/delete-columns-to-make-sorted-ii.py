class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        sp = [False] * (n - 1)          #   sp = sorted pairs
        d = 0                           #   d  = deletion

        for c in range(m):              #   c  = col
            dc = False                  #   dc = delete col
            
            for i in range(n - 1) :
                if not sp[i] and strs[i][c] > strs[i + 1][c] :
                    dc = True
                    break

            if dc :
                d += 1
                continue

            for i in range(n - 1) :
                if not sp[i] and strs[i][c] < strs[i + 1][c] :
                    sp[i] = True

        return d