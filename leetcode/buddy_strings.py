# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3492/
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        len_a = len(A)
        len_b = len(B)
        bad_tails = -1
        bad_starts = None
        
        if len_a != len_b:
            return False
        
        for i in range(0, len_a):
            if bad_starts is not None and i > bad_starts:
                continue
            # enough to check one character because previous ones were already checked
            if i > 0 and A[i-1] != B[i-1]:
                bad_starts = i
                #continue
                return False
                
            for j in range(len_a - 1, max(i, bad_tails), -1):
                if bad_tails is not None and j < bad_tails:
                    #print("inconceivable")
                    continue
                # enough to check one character because previous ones were already checked
                if j < len_a - 1 and A[j+1] != B[j+1]:
                    bad_tails = j
                    continue
                #print(str(A[:i] + A[j] + A[i+1:j] + A[i] + A[j+1:]))
                if A[j] == B[i] and A[i] == B[j] and A[i+1:j] == B[i+1:j]:
                # if str(A[j] + A[i+1:j] + A[i] + A[j+1:]) == B[i:]:
                    return True
        return False
