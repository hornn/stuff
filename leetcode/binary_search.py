# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3488/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if not length:
            return -1
        
        start = 0
        end = length - 1
        while end >= start:
            pivot = (end - start) // 2 + start
            val = nums[pivot]
            if target == val:
                return pivot
            elif target < val:
                end = pivot - 1
            else:
                start = pivot + 1
            #print(start, end)
        
        return -1
    
