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
    def connect_with_stack(self, root):
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

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return root

        # at every node, modify the next level's next field
        # then use the next field of this node (that were updated before) to skip to the next note
        # if there is no next field, skip to the next level (the first child of this level)

        itr = root
        next_level = None
        prev = None
        while itr:
            # print(itr.val, next_level.val if next_level else None, prev.val if prev else None)
            if itr.left:
                if prev:
                    prev.next = itr.left
                else:
                    next_level = itr.left
                prev = itr.left
            if itr.right:
                if prev:
                    prev.next = itr.right
                else:
                    next_level = itr.right
                prev = itr.right
            if itr.next:
                itr = itr.next
            else:
                itr = next_level
                next_level = None
                prev = None
        return root
