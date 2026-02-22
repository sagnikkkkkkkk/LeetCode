class Solution:
    def binaryGap(self, n: int) -> int:
        
        m = 0
        p = -1
        i = 0
        while n:
            if n & 1:
                if p != -1:
                    m = max(m , i-p)
                p = i
            n >>= 1
            i += 1
        return m