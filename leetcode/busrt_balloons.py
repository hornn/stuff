# https://leetcode.com/problems/burst-balloons/
class Solution:
    def maxCoins_naive(self, nums: List[int]) -> int:
            
            history = dict()
            
            def getMax(nums):
                nonlocal history
            
                # print(history)
                max_val = history.get(tuple(nums))
                if max_val is not None:
                    return max_val
                
                max_val = 0
                for idx in range(len(nums)):
                    if idx == 0:
                        prev = 1
                    else:
                        prev = nums[idx-1]
                    if idx == len(nums) - 1:
                        nxt = 1
                    else:
                        nxt = nums[idx+1]
                        
                    coins = nums[idx] * prev * nxt
                    new_nums = nums.copy()
                    new_nums.pop(idx)
                    val = coins + getMax(new_nums)
                    if val > max_val:
                        max_val = val
                history[tuple(nums)] = max_val
                # print(max_val, nums)
                return max_val
            # print(history)
            # remove zeros:
            nums = list(filter(lambda x: x != 0, nums))
            # print(nums)
            return getMax(nums)
        
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + list(filter(lambda x: x != 0, nums)) + [1]
        size = len(nums)
        dp = [[0] * size for _ in range(size)]
        
        def getMax(left, right):
            # print(left, right, dp)
            if dp[left][right]:
                return dp[left][right]
            
            out_of_range = nums[left-1] * nums[right+1]
            max_val = 0
            for i in range(left, right+1):
                max_val = max(max_val, nums[i] * out_of_range + getMax(left, i-1) + getMax(i+1, right))
            dp[left][right] = max_val
            return max_val
        
        return getMax(1, size-2)
                
