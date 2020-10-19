# https://leetcode.com/problems/house-robber/
class Solution(object):
    
    
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        
        length = len(nums)
        maxes = dict()
        
        def rob_by_idx(idx):
            max_val = maxes.get(idx)
            if max_val is not None:
                return max_val
            if idx >= length:
                return 0
            elif idx == length - 1:
                max_val = nums[idx]
            else:
                max_val = max(nums[idx] + rob_by_idx(idx+2), rob_by_idx(idx+1))
            maxes[idx] = max_val
            # print(idx, max_val)
            return max_val
        
        return rob_by_idx(0)
        
