class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        m = 10**9 + 7
        a = 0

        for i in range(1 , n+1):
            a = ((a << i.bit_length()) + i) % m

        return a