# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        prefix = {0: 1}   
        ans = 0

        def dfs(node, currSum):
            nonlocal ans

            if not node:
                return

            currSum += node.val

            ans += prefix.get(currSum - targetSum, 0)

            prefix[currSum] = prefix.get(currSum, 0) + 1

            dfs(node.left, currSum)
            dfs(node.right, currSum)

            prefix[currSum] -= 1

        dfs(root, 0)
        return ans



