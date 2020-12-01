# https://leetcode.com/problems/sliding-window-maximum/
# https://leetcode.com/problems/sliding-window-maximum/discuss/111560/Python-O(n)-solution-using-deque-with-comments
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        window = deque()
        
        res = []
        
        # initialize window
        for idx, num in enumerate(nums[:k]):
            # print(idx, num, curr_max)
            while window and nums[window[-1]] <= num:
                window.pop()
            
            window.append(idx)
     
        res.append(nums[window[0]])
        
                
        
        # print(window)

        for idx, num in enumerate(nums[k:]):
            idx += k
            # print(num, idx, window)
            # remove first value from window if out of bounds
            prev_max_idx = window[0]
            if prev_max_idx + k <= idx:
                reject = window.popleft()
                
            # remove low values from the right
            while window and nums[window[-1]] <= num:
                window.pop()
            
            window.append(idx)
            
            res.append(nums[window[0]])
            
        return res
