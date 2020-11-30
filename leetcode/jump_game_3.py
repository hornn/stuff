# https://leetcode.com/problems/jump-game-iii/
from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # find 0 indexes:
        zeros = set()
        for val, idx in enumerate(arr):
            if val == 0:
                zeros.add(idx)
                
        visited = set()
        stack = deque()
        stack.append(start)
        
        while stack:
            idx = stack.pop()
            print(idx, arr[idx], visited)
            if idx in visited:
                continue
            visited.add(idx)
            if arr[idx] == 0:
                return True
            
            plus = idx + arr[idx]
            minus = idx - arr[idx]
            if plus < len(arr):
                stack.append(plus)
            if minus >= 0:
                stack.append(minus)
        
        return False
        
