# https://leetcode.com/problems/game-of-life/
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return
        
        m = len(board)
        n = len(board[0])
        
        new_board = [[None] * n for _ in range(m)]
        # print(new_board)
        
        def live_neighbors(i, j):
            neighbors = 0
            # up
            if i > 0:
                if j > 0:
                    neighbors += board[i-1][j-1]
                neighbors += board[i-1][j]
                if j < n-1:
                    neighbors += board[i-1][j+1]
            # left
            if j > 0:
                neighbors += board[i][j-1]
            # down
            if i < m-1:
                if j > 0:
                    neighbors += board[i+1][j-1]
                neighbors += board[i+1][j]
                if j < n-1:
                    neighbors += board[i+1][j+1]
            
            # right
            if j < n-1:
                neighbors += board[i][j+1]
            # print(i,j,neighbors)
            return neighbors
                
        def calculate_pos(i, j):
            
            # Any live cell with fewer than two live neighbors dies as if caused by under-population.
            # Any live cell with two or three live neighbors lives on to the next generation.
            # Any live cell with more than three live neighbors dies, as if by over-population.
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            neighbors = live_neighbors(i, j)
            is_alive = board[i][j]
            if is_alive and 2 <= neighbors <= 3:
                new_pos = 1
            elif not is_alive and neighbors == 3:
                new_pos = 1
            else:
                new_pos = 0
            return new_pos
        
        
        for i in range(m):
            for j in range(n):
                new_board[i][j] = calculate_pos(i, j)
        
        
        
        # print(new_board)
        for i in range(m):
            board[i] = new_board[i]

