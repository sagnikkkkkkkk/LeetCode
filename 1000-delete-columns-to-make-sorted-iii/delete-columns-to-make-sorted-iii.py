class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])

        dp = [1] * m

        for j in range(m) :
            for i in range(j) :
                v = True                    #   v = valid
                for r in range(n):          #   r = row
                    if strs[r][i] > strs[r][j] :
                        v = False
                        break

                if v :
                    dp[j] = max(dp[j] , dp[i] + 1)

        mk = max(dp)                        #   mk = max keep

        return m - mk