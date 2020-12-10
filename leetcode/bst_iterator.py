# https://leetcode.com/problems/binary-search-tree-iterator/

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    arr = []
    it = 0
    
    def scan(self, root):
        if not root:
            return []
        return self.scan(root.left) + [root.val] + self.scan(root.right)
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = self.scan(root)
        self.it = 0
                
    def next(self):
        """
        :rtype: int
        """
        val = self.arr[self.it]
        self.it += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.it < len(self.arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
