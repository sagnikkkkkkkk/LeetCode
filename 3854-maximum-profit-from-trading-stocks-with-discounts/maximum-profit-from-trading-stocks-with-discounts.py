class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:

        from collections import defaultdict

        tree = defaultdict(list)
        for u , v in hierarchy :
            tree[u - 1].append(v - 1)

        NEG = -10**9

        def dfs(u) :
            dp0 = [0] + [NEG] * budget
            dp1 = [0] + [NEG] * budget

            for v in tree[u] :
                c0 , c1 = dfs(v)
                new0 = [NEG] * (budget + 1)
                new1 = [NEG] * (budget + 1)

                for i in range(budget + 1) :
                    if dp0[i] > NEG :
                        for j in range(budget - i + 1) :
                            if c0[j] > NEG :
                                new0[i + j] = max(new0[i + j] , dp0[i] + c0[j])
                    if dp1[i] > NEG :
                        for j in range(budget - i + 1) :
                            if c1[j] > NEG :
                                new1[i + j] = max(new1[i + j] , dp1[i] + c1[j])
            
                dp0 , dp1 = new0 , new1

            full_cost = present[u]
            disc_cost = present[u] // 2
            full_profit = future[u] - full_cost
            disc_profit = future[u] - disc_cost

            res_parent_no_buy = list(dp0)
            res_parent_buy = list(dp0)

            for c in range(budget , -1 , -1) :
                if c >= full_cost and dp1[c - full_cost] > NEG :
                    res_parent_no_buy[c] = max(res_parent_no_buy[c] , dp1[c - full_cost] + full_profit)
                if c >= disc_cost and dp1[c - disc_cost] > NEG :
                    res_parent_buy[c] = max(res_parent_buy[c] , dp1[c - disc_cost] + disc_profit)
            
            return res_parent_no_buy , res_parent_buy

        root_res, _ = dfs(0)
        return max(0 , max(root_res))