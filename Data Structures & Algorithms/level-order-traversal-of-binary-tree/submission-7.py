# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ret = []

        def bfs(root):
            q = deque()
            if root:
                q.append(root)
            
            while q:
                res = []
                for _ in range(len(q)):
                    curr = q.popleft()
                    res.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                ret.append(res)
        
        bfs(root)
        return ret