# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(n,v):
            if not n:
                return 0

            v = (v << 1) | n.val

            if not n.left and not n.right:
                return v

            return dfs(n.left , v) + dfs(n.right , v)

        return dfs(root , 0)