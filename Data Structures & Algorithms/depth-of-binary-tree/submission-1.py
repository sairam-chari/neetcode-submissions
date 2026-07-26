# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxd=0
        def recc(node,d):
            if not node or not (node.left or node.right):
                return d
            if node.left or node.right:
                return max(recc(node.left,d+1),recc(node.right,d+1))
                
            # return 0
        if not root:
            return 0
        return recc(root,1)

        