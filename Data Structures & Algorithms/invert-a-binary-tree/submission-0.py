# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Once finished, return the root
        return root