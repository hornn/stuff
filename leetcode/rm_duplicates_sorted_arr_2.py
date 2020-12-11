# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 2:
            return size;
        
        pointer = 1
        count = 1
        curr_val = nums[0]
        for idx in range(1, size):
            new_val = nums[idx]
            if new_val == curr_val:
                count += 1
                if count > 2:
                    continue  # not copy 
            else:
                curr_val = new_val
                count = 1
            if idx > pointer:
                nums[pointer] = nums[idx]
            pointer += 1
            # print(nums, pointer)
        return pointer
