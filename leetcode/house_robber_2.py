# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3494/
class Solution(object):
    
    def rob_row(self, nums):
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
        
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # examples:
        # [1,2,3,4] => 1+3, 2+4. can_use_last = True
        # [1,2,3,4,5] => 1+3, 2+4, 3+5, 4+1
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob_row(nums[:-1]), self.rob_row(nums[1:]))
#         len_list = len(nums)
#         can_use_last = bool(len_list % 2 == 0)
        
#         even_sum = 0
#         odd_sum = 0
#         for num, idx in enumerate(nums):
#             if idx % 2 == 0:
#                 even_sum += num
    
        
