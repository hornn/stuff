# https://leetcode.com/problems/spiral-matrix-ii/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        matrix = [None] * n
        for idx in range(n):
            matrix[idx] = [0] * n
            
        matrix[0][0] = 1
        x = 0
        y = 0
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3
        direction = RIGHT
        for num in range(2, n*n + 1):
            # print(x, y, direction, matrix)
            while True:
                if direction == RIGHT:
                    if y + 1 < n and matrix[x][y+1] == 0:
                        y += 1
                        matrix[x][y] = num
                        break
                    else:
                        direction = DOWN
                if direction == DOWN:
                    if x + 1 < n and matrix[x+1][y] == 0:
                        x += 1
                        matrix[x][y] = num
                        break
                    else:
                        direction = LEFT
                if direction == LEFT:
                    if y - 1 >= 0 and matrix[x][y-1] == 0:
                        y -= 1
                        matrix[x][y] = num
                        break
                    else:
                        direction = UP
                if direction == UP:
                    if x - 1 >= 0 and matrix[x-1][y] == 0:
                        x -= 1
                        matrix[x][y] = num
                        break
                    else:
                        direction = RIGHT
            
                    
        return matrix
