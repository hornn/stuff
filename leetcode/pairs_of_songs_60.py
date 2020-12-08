# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from collections import defaultdict

class Solution(object):
    def numPairsDivisibleBy60_on2(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        if not time:
            return 0
        
        res = 0
        
        for i, song in enumerate(time):
            
            for j in range(i+1, len(time)):
                
                if (song + time[j]) % 60 == 0:
                    res += 1
        return res
    
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        if not time:
            return 0
        
        res = 0
        counts = defaultdict(int)
        
        # count all songs by their %60 values. 
        for song in time:
            mod = song % 60
            counts[mod] += 1
        
        # count pairs that match to 60 (i*j)
        # the songs in bucket 0 (e.g. 60) pair with each other sum(1..n-1)
        if counts[0] > 1:
            for i in range(1, counts[0]):
                res += i
        if counts[30] > 1:
            for i in range(1, counts[30]):
                res += i
        for i in range(1, 30):
            j = 60 - i
            count_i = counts[i]
            count_j = counts[j]
            if count_i and count_j:
                res += (count_i * count_j)
     
        return res
