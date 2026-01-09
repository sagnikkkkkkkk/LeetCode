# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(n):
            if not n:
                return(0,None)
            
            ld , ln = dfs(n.left)
            rd , rn = dfs(n.right)

            if ld > rd:
                return (ld+1 , ln)
            elif rd > ld:
                return (rd+1 , rn)
            else: 
                return (ld+1 , n)

        return dfs(root)[1]