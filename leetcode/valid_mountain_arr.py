# https://leetcode.com/problems/valid-mountain-array/

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        
        # there should be a increase in the first step
        if arr[0] >= arr[1]:
            return False
        
        should_be_inc = True        
        
        for idx in range(2, len(arr)):
            first = arr[idx-1]
            second = arr[idx]
            # print(first, second)
            if first == second:
                return False
            
            if should_be_inc:
                if first < second:
                    continue
                else:  # first > second
                    should_be_inc = False
                    continue
            else:
                if first <= second:
                    return False
        
        return not should_be_inc
