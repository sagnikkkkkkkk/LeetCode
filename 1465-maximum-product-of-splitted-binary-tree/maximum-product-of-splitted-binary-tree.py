class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        m = 10**9 + 7               #   m = mod
        self.max_prod = 0

        def ts(n):                  #   ts = total sum
            if not n:
                return 0
            return n.val + ts(n.left) + ts(n.right)

        t = ts(root)

        def dfs(n):
            if not n:
                return 0

            left = dfs(n.left)
            right = dfs(n.right)

            ss = n.val + left + right           #   ss = sub sum

            self.max_prod = max(
                self.max_prod , 
                ss * (t - ss)
            )

            return ss

        dfs(root)
        return self.max_prod % m


























