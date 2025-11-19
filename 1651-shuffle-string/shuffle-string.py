class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for c,i in zip(s,indices) : 
            res[i] = c
        return "".join(res)