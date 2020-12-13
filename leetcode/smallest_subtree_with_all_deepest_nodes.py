# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
from collections import namedtuple
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # find depth of each node
        
        # save each node's depth as well as its parents
        
        # for the deepest nodes, look at their common parents and choose the one with the highest depth itself.
        
        DepthAndParents = namedtuple('DepthAndParents', 'depth parents node')
        
        max_depth = 0
        deepest_nodes = set()
        
        node_stats = dict()
        
        def dfs(node, parent):
            nonlocal max_depth, deepest_nodes, node_stats
            if not node:
                return set()
            parent_stats = node_stats.get(parent, DepthAndParents(0, set(), None))
            depth = parent_stats.depth + 1
            if max_depth == depth:
                deepest_nodes.add(node.val)
            elif max_depth < depth:
                max_depth = depth
                deepest_nodes = {node.val}
            parents = parent_stats.parents | {node.val}
            node_stats[node.val] = DepthAndParents(depth, parents, node)
            dfs(node.left, node.val)
            dfs(node.right, node.val)
        
        dfs(root, -1)
        # print(node_stats)
        # print(max_depth, deepest_nodes)
        
        common_parents = set()
        for node in deepest_nodes:
            stats = node_stats[node]
            if not common_parents:
                common_parents = stats.parents
            else:
                common_parents &= stats.parents
        # print(common_parents)
        
        max_parent_depth = 0
        sub_tree = None
        for parent in common_parents:
            stats = node_stats[parent]
            if max_parent_depth < stats.depth:
                max_parent_depth = stats.depth
                sub_tree = stats.node
        # print(max_parent_depth, sub_tree)
        
        return sub_tree
            
