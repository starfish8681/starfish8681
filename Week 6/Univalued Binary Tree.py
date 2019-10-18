#A binary tree is univalued if every node in the tree has the same value.
#Return true if and only if the given tree is univalued.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        vals = []

        def dfs(node): #若node非0或Null
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1  #不重複的數數量是否為1
