class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        r = []

        while i >= 0 or j >= 0 or c:
            
            s = c

            if i >= 0:
                s += int(a[i])
                i -= 1

            if j >= 0:
                s += int(b[j])
                j -= 1

            r.append(str(s % 2))
            c = s // 2

        return ''.join(r[::-1])