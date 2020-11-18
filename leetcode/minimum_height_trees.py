# https://leetcode.com/problems/minimum-height-trees
# naive solution - calculate height for each root in a loop

from collections import defaultdict, deque

class Solution(object):
    
    
    def calculate_max_height(self, vertices, root, current_min):
        stack = deque()
        stack.append((root, 0))
        
        visited = set()
        max_height = 0
        while stack:
            v, height = stack.pop()
            #print(v, height)
            max_height = max(height, max_height)
            # short-circuit
            if max_height > current_min:
                return False
            visited.add(v)
            children = vertices[v] - visited
            c_height = height + 1
            # short-circuit 2
            if children and c_height > current_min:
                return False
            for child in children:
                stack.append((child, c_height))
        return max_height
    
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return list(range(n))
        
        vertices = defaultdict(set)
        
        # build tree
        for edge in edges:
            x = edge[0]
            y = edge[1]
            vertices[x].add(y)
            vertices[y].add(x)
        #print(vertices)
        
        current_min = n/2 + 1
        print(current_min)
        current_min_roots = []
        
        # for each vertex, calcuate max height starting from it as root
        for v in range(n):
            # if the height exceeds the current min, break and return False. 
            # Otherwise return the tree's max height (which can be equal or less than the current min)
            max_height = self.calculate_max_height(vertices, v, current_min)
            if max_height is False:
                continue
            elif max_height == current_min:
                current_min_roots.append(v)
            elif max_height < current_min:
                current_min = max_height
                current_min_roots = [v]
            else:
                raise Exception('error in calculating %d. (max = %s)' % (v, max_height))
            
        #print(current_min_roots, current_min)
        return current_min_roots
                
            
