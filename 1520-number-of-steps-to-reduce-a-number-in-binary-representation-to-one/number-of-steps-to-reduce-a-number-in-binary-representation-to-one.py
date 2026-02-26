class Solution:
    def numSteps(self, s: str) -> int:
        r = 0
        c = 0

        for i in range(len(s) - 1 , 0 , -1):
            if int(s[i]) + c == 1:
                r += 2
                c = 1
            else:
                r += 1

        return r+c