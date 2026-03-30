# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_val):
            if not root:
                return 0

            res = 0
            if max_val <= root.val:
                res = 1
            new_max = max(max_val, root.val)
            res += dfs(root.left, new_max)
            res += dfs(root.right, new_max)
            return res
        
        return dfs(root, root.val)