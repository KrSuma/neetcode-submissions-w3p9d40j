# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        res = []

        def checkPathSum(root, res, targetSum):
            if not root:
                return False
            res.append(root.val)
            if not root.left and not root.right:
                is_sum = sum(res) == targetSum
                if not is_sum: 
                    res.pop()
                return is_sum
            if checkPathSum(root.left, res, targetSum):
                return True
            if checkPathSum(root.right, res, targetSum):
                return True
            res.pop()
            return False

        return checkPathSum(root, res, targetSum)
