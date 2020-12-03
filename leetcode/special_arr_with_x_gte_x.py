# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
from collections import defaultdict

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = defaultdict(int)
        length = len(nums)
        for num in nums:
            if num < length:
                sums[num] += 1
            else:
                sums[length] +=1
        # print(sums)
        if sums[length] == length:
            return length
        for idx in range(length-1, -1, -1):
            sums[idx] += sums[idx+1]
            if idx == sums[idx]:
                return idx
        # print(sums)
        return -1
