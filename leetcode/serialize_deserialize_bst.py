#https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3489/
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ''
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.popleft()
            res.append(str(node.val))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        #print(res)
        return ','.join(res)
       
    
   
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split(',')
        arr = [int(x) for x in arr]
        #print(arr)
   
        def insertToRoot(val, root):
            #print(val, root)
            if val == root.val:
                return
            elif val < root.val:
                if root.left:
                    return insertToRoot(val, root.left)
                else:
                    root.left = TreeNode(val)
                    return
            else:
                if root.right:
                    return insertToRoot(val, root.right)
                else:
                    root.right = TreeNode(val)
                    return

        def printTree(root):
            res = ''
            stack = deque()
            stack.append(root)
            while stack:
                node = stack.popleft()
                res += ' ' + str(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            #print(res)

        root = TreeNode(arr[0])
        for val in arr[1:]:
            #printTree(root)
            insertToRoot(val, root)  
        #printTree(root)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
