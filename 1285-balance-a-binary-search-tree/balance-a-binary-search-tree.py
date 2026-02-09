class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        v = []

        def dfs(x):
            if not x:
                return
            dfs(x.left)
            v.append(x.val)
            dfs(x.right)

        def bst(l , r):
            if l > r:
                return None
            m = (l + r) // 2
            t = TreeNode(v[m])
            t.left = bst(l , m-1)
            t.right = bst(m+1 , r)
            return t

        dfs(root)
        return bst(0 , len(v) - 1)
