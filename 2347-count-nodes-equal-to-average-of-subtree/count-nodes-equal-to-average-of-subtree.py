# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(x):
            if not x:
                return (0, 0)
            lc, l = dfs(x.left)
            rc, r = dfs(x.right)
            if x.val == (l+r+x.val)//(lc+rc+1):
                self.count += 1
            return (lc+rc+1, l+r+x.val)
        dfs(root)
        return self.count
        