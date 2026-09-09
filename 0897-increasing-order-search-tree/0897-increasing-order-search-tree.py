# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root):
        self.prev = None
        self.first = None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev:
                self.prev.right = node
            else:
                self.first = node
            node.left = None
            self.prev = node
            inorder(node.right)
        inorder(root)
        return self.first