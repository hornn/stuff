# https://leetcode.com/problems/crawler-log-folder/
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        depth = 0
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if depth > 0:
                    depth -= 1
            else:
                depth += 1
                
        return depth

