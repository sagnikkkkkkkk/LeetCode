class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        p = 0
        c = 1
        a = 0

        for i in range(1 , len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                a += min(p , c)
                p = c
                c = 1

        a += min(p , c)
        return a