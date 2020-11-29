# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

from collections import defaultdict

class Solution(object):
    
    def longestSubstring_n3(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        
        max_len = 0
        
        def check_if_sub(i, j):
            counts = defaultdict(int)
            for x in s[i: j+1]:
                counts[x] += 1
            print(i,j, counts)
            return all(val >= k for val in counts.values())
        
        # check each possible substring
        for i in range(0, len(s) - k+1):
            for j in range(len(s)-1, i + k - 2, -1):
                if max_len >= (j-i+1):
                    continue
                is_sub = check_if_sub(i, j)
                if is_sub:
                    max_len = max(max_len, j-i+1)
        return max_len
    
    
    def longestSubstring_n2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # for each iteration, save the counts to be used by the next one
        if len(s) < k:
            return 0
        
        max_len = 0
        counts = defaultdict(int)
        current_x = 0
        
        def check_if_sub(i, j):
            counts[s[j]] += 1
            # for x in s[j]:
                # counts[x] += 1
            current_x = j+1
            print(i,j, counts)
            return all(val >= k for val in counts.values())
        
        # check each possible substring
        for i in range(0, len(s) - k+1):
            counts = defaultdict(int)
            current_x = i
            for j in range(i, len(s)):
            # for j in range(i + k, len(s)):
            # for j in range(len(s)-1, i + k - 2, -1):
                 # max_len >= (j-i+1):
                    # continue
                is_sub = check_if_sub(i, j)
                if is_sub:
                    max_len = max(max_len, j-i+1)
        return max_len
    
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # print(s, k)
        
        if len(s) < k:
            return 0
        
        # count frequencies:
        counts = defaultdict(int)
        for letter in s:
            counts[letter] += 1
        # print counts
        
        # get bad letters:
        bads = set()
        for letter, freq in counts.items():
            if freq < k:
                bads.add(letter)
        # print(bads)
        if not bads:
            return len(s)
        
        # calculate on each of the substrings without the bad chars
        max_len = 0
        start = 0
        end = 0
        for letter in s:
            if letter in bads:
                max_len = max(max_len, self.longestSubstring(s[start:end], k))
                start = end + 1
                end = start
            else:
                end += 1
        max_len = max(max_len, self.longestSubstring(s[start:end], k))
        return max_len
            
