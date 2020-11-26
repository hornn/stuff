# https://leetcode.com/problems/maximal-square/
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        visited = set()
        len_x = len(matrix)
        if not len_x:
            return 0
        len_y = len(matrix[0])
        if not len_y:
            return 0
        
        def find_max_sq_from_point(x, y):
            # print(x,y, matrix[x][y])
            if matrix[x][y] == '0':
                return 0
            size = 1
            while y + size < len_y and x + size < len_x:
                # check line below:
                for yy in range(y, y+size+1):
                    if matrix[x+size][yy] == '0':
                        return size
                for xx in range(x, x+size+1):
                    if matrix[xx][y+size] == '0':
                        return size
                size += 1
                # print(size)
            return size
        
        max_size = 0
        for x in range(0, len_x):
            for y in range(0, len_y):
                new_size = find_max_sq_from_point(x, y)
               # print(new_size)
                max_size = max(max_size, new_size)
                
        return max_size * max_size
            
                
        
