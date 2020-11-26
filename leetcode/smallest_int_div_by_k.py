# https://leetcode.com/problems/smallest-integer-divisible-by-k/
class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        mod = 0
        for i in range(1, K+1):
            mod = (mod * 10 + 1) % K
            if mod == 0:
                return i
        return -1
    
    
        # explanation:
        # 11111 = 1111 * 10 + 1
        # 11111 % k = (1111 * 10 + 1) % k = 
        #             ((1111 * 10) %k + 1 %k ) % k
        #             (((1111 %k) * 10) + 1) % k
        # and (1111 %k) is the previous iteration's mod
        
