# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxval):
            if not root:
                return 0

            res = 0
            if root.val >= maxval:
                res = 1
            curmax = max(root.val, maxval)
            
            res += dfs(root.left, curmax)
            res += dfs(root.right, curmax)

            return res
            
        return dfs(root, root.val)