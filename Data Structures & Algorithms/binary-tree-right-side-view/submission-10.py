# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ret = []

        def bfs(root):
            q = deque()
            if root:
                q.append(root)
            
            while q:
                rightmost_val = 0
                for _ in range(len(q)):
                    curr = q.popleft()
                    # res.append(curr.val)
                    rightmost_val = curr.val
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                ret.append(rightmost_val)
        
        bfs(root)
        return ret