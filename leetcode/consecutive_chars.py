# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3518/
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        power = 0
        
        current_letter = s[0]
        current_streak = 1
        
        for letter in s[1:]:
            if letter == current_letter:
                current_streak += 1
            else:
                power = max(current_streak, power)
                current_letter = letter
                current_streak = 1
        
        power = max(current_streak, power)
        return power
