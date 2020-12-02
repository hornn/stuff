# https://leetcode.com/problems/shortest-distance-to-a-character/
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        if not S or C not in S:
            raise Exception("wrong input")
            
        c_idxs = []
        for idx, x in enumerate(S):
            if x == C:
                c_idxs.append(idx)
        
        res = []
        next_c = 0
        next_c_idx = c_idxs[next_c]
        prev_c_idx = None
        for idx in range(len(S)):
            if idx == next_c_idx:
                dist = 0
                next_c += 1
                prev_c_idx = next_c_idx
                next_c_idx = c_idxs[next_c] if next_c < len(c_idxs) else None
                                
            elif next_c_idx is not None:
                assert idx < next_c_idx
                if prev_c_idx is not None:
                    dist = min(idx - prev_c_idx, next_c_idx - idx)
                else:
                    dist = next_c_idx - idx
            else:
                assert prev_c_idx is not None and idx > prev_c_idx, prev_c_idx
                dist = idx - prev_c_idx
                                
            res.append(dist)
            # print(res, prev_c_idx, next_c_idx)
        return res
            
