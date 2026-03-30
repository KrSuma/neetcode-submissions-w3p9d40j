# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_value):
            if not root:
                return 0
            
            is_good = 0
            if max_value <= root.val:
                is_good = 1
            new_max = max(max_value, root.val)

            return is_good + dfs(root.left, new_max) + dfs(root.right, new_max) 
        
        return dfs(root, float('-inf'))