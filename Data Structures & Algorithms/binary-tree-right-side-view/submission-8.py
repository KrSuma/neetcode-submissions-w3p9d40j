
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ret = []

        q = deque()
        if root:
            q.append(root)
        while len(q) > 0:
            res = []
            for _ in range(len(q)):
                curr = q.popleft()
                res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ret.append(res[-1])
        
        return ret