class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        res = []

        def dfs(s):
            if len(res) >= k:
                return

            if len(s) == n:
                res.append(s)
                return
            
            for ch in ['a' , 'b' , 'c']:
                if not s or s[-1] != ch:
                    dfs(s + ch)

        dfs("")

        return res[k-1] if k <= len(res) else ""