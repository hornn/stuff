# https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict, deque

class Solution(object):
    
    @staticmethod
    def findLeaves(vertices):
        leaves = set()
        for v, edges in vertices.items():
            if len(edges) == 1:
                leaves.add(v)
        return leaves
    
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return list(range(n))
        
        # build graph:
        vertices = defaultdict(set)
        for edge in edges:
            x = edge[0]
            y = edge[1]
            vertices[x].add(y)
            vertices[y].add(x)
        
        #print(vertices)
        # find leaves:
        leaves = Solution.findLeaves(vertices)
        #print(leaves)
        
        remaining_num = n
        
        while remaining_num > 2:
            remaining_num -= len(leaves)
            
            for leaf in leaves:
                # remove the edge of this leaf - there should be exactly 1
                neighbours = vertices[leaf]
                assert len(neighbours) == 1
                neighbour = next(iter(neighbours))
                vertices[neighbour].remove(leaf)
                del vertices[leaf]
            #print(vertices)
                
            leaves = Solution.findLeaves(vertices)
            
        #print(vertices)
        return vertices.keys()
