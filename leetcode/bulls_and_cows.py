# https://leetcode.com/problems/bulls-and-cows/
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        secret_count = dict()
        guess_count = dict()
        # find exact matches, and count the frequency of the other letters:
        bulls = 0
        for idx, (x, y) in enumerate(zip(secret, guess)):
            if x == y:
                bulls += 1
            else:
                secret_count[x] = secret_count.get(x, 0) + 1
                guess_count[y] = guess_count.get(y, 0) + 1
        
        cows = 0
        
        # calculate the cows - the number of cows is the min between the secret frequency and guess frequency of each letter.
        for key, g_count in guess_count.items():
            s_count = secret_count.get(key, 0)
            cows += min(g_count, s_count)
            
        return "%dA%dB" % (bulls, cows)
        
            
        
