class Solution:
    def minOperations(self, s: str) -> int:
        
        a = b = 0

        for i in range(len(s)):
            if s[i] != str(i % 2):
                a += 1
            if s[i] != str((i + 1) % 2):
                b += 1

        return min(a , b)