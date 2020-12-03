# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def parse(self, node):
        if not node:
            return []
        return self.parse(node.left) + [node.val] + self.parse(node.right)
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        arr = self.parse(root)
        # print(arr)
        
        node = None
        for x in reversed(arr):
            node = TreeNode(x, None, node)
        # print(node)
        return node
        
