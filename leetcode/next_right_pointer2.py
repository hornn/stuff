# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        stack = []
        stack.append(root)
        
        # add nodes of each lvel from right to left, for ease of use when populating the nexts.
        
        while stack:
            # print([node.val for node in stack])
            new_queue = []
            next_node = None
            for node in stack:
                node.next = next_node
                next_node = node
                if node.right:
                    new_queue.append(node.right)
                if node.left:
                    new_queue.append(node.left)
            stack = new_queue
            
        return root
