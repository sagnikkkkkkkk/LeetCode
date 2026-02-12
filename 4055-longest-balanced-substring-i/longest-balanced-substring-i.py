class Solution:
    def longestBalanced(self, s: str) -> int:
        
        n = len(s)
        r = 0

        for i in range(n):
            f = [0]*26
            d = 0
            m = 0

            for j in range(i , n):
                k = ord(s[j]) - 97

                if f[k] == 0:
                    d += 1

                f[k] += 1
                m = max(m , f[k])

                if (j - i + 1) == d*m:
                    r = max(r , j-i+1)

        return r