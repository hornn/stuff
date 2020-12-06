# https://leetcode.com/problems/can-place-flowers/

from collections import deque

class Solution(object):
    
    def canPlaceFlowers_recursive(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        # print(flowerbed, n)
        size = len(flowerbed)
        visited = dict()
        
        def can_place(start, n):
            if visited.get((start, n)):
                return False
            
            visited[(start, n )] = True
            
            print(start, n)
            if n == 0:
                return True

            if start >= size:  
                # n > 0 so not enough place for flowers
                return False 

            if start == size - 1:
            # if len(flowerbed) == 1:
                # only one more room for flower
                return flowerbed[start] == 0 and n == 1

            first = flowerbed[start]
            second = flowerbed[start+1]
            if first == 1:
                return can_place(start+2, n)
            elif second == 1:  # first == 0
                return can_place(start+1, n)
            else:  # first == 0 and second == 0:
                # try to place flower on first, or try without placing flower on first
                return can_place(start+2, n-1) or can_place(start+1, n)
        
        return can_place(0, n)
    
    def canPlaceFlowers_stack(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        # print(flowerbed, n)
        size = len(flowerbed)
        visited = dict()
        
        stack = deque()
        stack.append((0, n))
        
        while stack:
            (start, n) = stack.pop()
            if visited.get((start, n)):
                continue
            visited[(start, n)] = True
            
            # print(start, n)
            if n == 0:
                return True
            if start >= size or (size-start+1)/2 < n:
                continue
                
            if start == size - 1:
                if flowerbed[start] == 0 and n == 1:
                    return True
                else:
                    continue
                
            
            first = flowerbed[start]
            second = flowerbed[start+1]
            if first == 1:
                stack.append((start+2, n))
                # return can_place(start+2, n)
            elif second == 1:  # first == 0
                stack.append((start+1, n))
                # return can_place(start+1, n)
            else:  # first == 0 and second == 0:
                # try to place flower on first, or try without placing flower on first
                stack.append((start+2, n-1))
                stack.append((start+1, n))
                # return can_place(start+2, n-1) or can_place(start+1, n)
            
        return False
    
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # just iterate through and put 1 whenever possible
        if n == 0:
            return True
        
        count = 0
        size = len(flowerbed)
        
        for idx in range(size):
            # print(flowerbed)
            if flowerbed[idx] == 1:
                continue
            # empty plot - check neighbours:
            if (idx == 0 or flowerbed[idx-1] == 0) and (idx == size-1 or flowerbed[idx+1] == 0):
                flowerbed[idx] = 1
                count +=1
            if count == n:
                return True
        return (count == n)
            
    
    
