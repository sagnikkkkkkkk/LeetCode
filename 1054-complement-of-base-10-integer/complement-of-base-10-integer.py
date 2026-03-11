class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1

        b = bin(n)[2:]
        s = ""

        for c in b:
            if c == '0':
                s += '1'

            else:
                s += '0'

        return int(s,2)