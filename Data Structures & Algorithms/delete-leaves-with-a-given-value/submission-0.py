
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        node = root

        def dfs(root, target):
            if not root:
                return None

            root.left = dfs(root.left, target)
            root.right = dfs(root.right, target)
            
            if not root.left and not root.right:
                if root.val == target:
                    return None

            return root
        
        return dfs(node, target)
