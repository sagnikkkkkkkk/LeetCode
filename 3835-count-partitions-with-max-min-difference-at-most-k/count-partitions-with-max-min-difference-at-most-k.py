class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        MOD = 10**9 + 7
        n   = len(nums)

        dp    = [0] * (n+1)
        dp[0] =  1

        pref    =   [0] * (n+2)
        pref[0] =    0
        pref[1] = dp[0]

        maxdp = deque()
        mindq = deque()
        left = 0

        for r in range(n) :
            while maxdp and nums[maxdp[-1]] <= nums[r] :
                maxdp.pop()
            maxdp.append(r)

            while mindq and nums[mindq[-1]] >= nums[r] :
                mindq.pop()
            mindq.append(r)

            while nums[maxdp[0]] - nums[mindq[0]] > k :
                if maxdp[0] == left :
                    maxdp.popleft()
                if mindq[0] == left :
                    mindq.popleft()
                left += 1 
            
            ways        = (pref[r + 1] - pref[left]) % MOD
            dp[r + 1]   =  ways
            pref[r + 2] = (pref[r + 1] +  dp[r + 1]) % MOD
        
        return dp[n]


