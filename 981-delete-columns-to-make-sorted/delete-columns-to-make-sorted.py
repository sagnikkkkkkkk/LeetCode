class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        r = len(strs)               #   r = rows
        c = len(strs[0])            #   c = cols
        a = 0                       #   a = answer

        for p in range(c) :
            for q in range(r - 1) :
                if strs[q][p] > strs[q + 1][p] :
                    a += 1
                    break

        return a