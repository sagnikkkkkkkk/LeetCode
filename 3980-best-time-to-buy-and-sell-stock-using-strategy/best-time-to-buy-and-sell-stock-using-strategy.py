class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        
        n = len(prices)

        b_p = 0         # b_p = base_profit

        for i in range(n) :
            b_p += strategy[i] * prices[i]

        half = k // 2

        dt = 0          # dt = delta

        for i in range(half) :
            dt += (0 - strategy[i]) * prices[i]

        for i in range(half , k) :
            dt += (1 - strategy[i]) * prices[i]

        M_dt = dt           # M_dt = max_delta

        for l in range(1 , n - k + 1) :
            dt -= (0 - strategy[l - 1]) * prices[l - 1]

            m_idx = l + half - 1           # m_idx = mid_idx

            dt -= (1 - strategy[m_idx]) * prices[m_idx]
            dt += (0 - strategy[m_idx]) * prices[m_idx]

            n_idx = l + k - 1           # n_idx = new_idx
            dt += (1 - strategy[n_idx]) * prices[n_idx]

            if dt > M_dt : 
                M_dt = dt

        return b_p + max(0 , M_dt)