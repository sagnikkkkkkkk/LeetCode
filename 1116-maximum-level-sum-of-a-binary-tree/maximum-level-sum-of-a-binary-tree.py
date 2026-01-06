# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
                                
        q = [root]              #   q = queue
        l = 1                   #   l = level
        ms = -10**18            #   ms = max sum
        a = 1                   #   a = answer

        while q:
            ls = 0              #   ls = level sum
            nl = []             #   nl = next level

            for n in q:         #   n = node
                ls += n.val
                if n.left:
                    nl.append(n.left)
                if n.right:
                    nl.append(n.right)    
            
            if ls > ms:
                ms = ls
                a = l

            q = nl
            l += 1

        return a