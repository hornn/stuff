#https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch_draft1(self, s, p):
        """
        this solution fails to solve s="aaa", p="a*a" because it doesn't handle non greedy cases.
        
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if p == '.*':
            return True
        
        if not s or not p:
            return s == p
        
        p_idx = 0
        p_len = len(p)
        s_idx = 0
        s_len = len(s)
        
        p_val = p[0]
        p_star = False
        if p_idx+1 < p_len and p[p_idx+1] == '*':
            p_idx += 1
            p_star = True
        
        while s_idx < s_len:
            letter = s[s_idx]            
            # need to check 4 cases:
            # 1. letter == p[idx]
            # 2. letter == p[idx] and p[idx+1] == '*'
            # 3. p[idx] == '.'
            # 4. p[idx] == '.' and p[idx+1] == '*'
            if letter == p_val or p_val == '.':
                s_idx += 1
                if not p_star:
                    p_idx += 1
                    if p_len <= p_idx:
                        break
                    p_val = p[p_idx]
                    p_star = (p_idx+1 < p_len and p[p_idx+1] == '*')
                    if p_star:
                        p_idx += 1
            # if there is no match with *, move to the next part of the pattern
            elif p_star:
                p_idx += 1
                if p_len <= p_idx:
                    break
                p_val = p[p_idx]
                p_star = (p_idx+1 < p_len and p[p_idx+1] == '*')
                if p_star:
                    p_idx += 1
            else:
                return False
        if p_star:
            p_idx += 1
        return s_idx == s_len and p_idx == p_len
                
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        """
        new idea: take p and expand it to all possible expressions.
        e.g. a*a will be expanded to: a, aa, aaa, aaaa, etc. until the length of s.
        then go over the solutions and compare to s.
        
        comparison can be smart - i.e. if the beginning doesn't match, the whole branch of expansions is not possible.
        expansion can be done on the fly, i.e. start with the first letter of s, and expand only patterns that match that letter.
        """
        
        def check_part_string(s, p):
            """ 
            :param s: part of string to check match
            :param p: expanded pattern to match to: either a, aa, aaa, etc. or ., ., ..., etc.
            """
            #print(s, p)
            return s == p or (all(pp == '.' for pp in p) and len(s) == len(p))
           
        
        def find_match(s, p_list):
            """
            :param s: string to match
            :param p_list: list of pattern parts. devided to chars (a/.) and char+* (a*/.*)
            """
            
            #print("find_match(s=%s, p_list=%s)" % (s, p_list))
            
            if not p_list:
                return s == ''  # if there are no more parts to match and the string is empty we matched everything
            
            number_of_necessary_chars = len([p for p in p_list if '*' not in p])
            #print(number_of_necessary_chars)
            
            p = p_list[0]
            p_char = str(p[0])
            if '*' in p:
                p_part = ''
                for s_idx in range(0, len(s) + 1 - number_of_necessary_chars):
                    s_part = str(s[:s_idx])
                    # expand pattern: x* with idx=2 will be expanded to xx
                    #p_part = ''.join([p_char] * s_idx)
                    
                    #print(p_part, s_part)
                    if check_part_string(s_part, p_part):
                        match = find_match(s[s_idx:], p_list[1:])
                        if match:
                            return True
                    p_part += p_char
            else:
                s_part = str(s[:1])
                p_part = p_char
                #print(p_part)
                if check_part_string(s_part, p_part):
                    match = find_match(s[1:], p_list[1:])
                    if match:
                        return True
            return False
                        
        def parse_pattern(p):
            p_list = []
            p_part = ''
            for c in p:
                if c == '*':
                    p_part += c
                    p_list.append(p_part)
                    p_part = ''
                else:
                    if p_part:
                        p_list.append(p_part)
                    p_part = c
            if p_part:
                p_list.append(p_part)
            #print(p_list)
            p_list = [str(p) for p in p_list]
            #print(p_list)
            return p_list
        
        # sanity:
        if '**' in p or p.startswith('*'):
            return False
        
        p_list = parse_pattern(p)
        return find_match(s, p_list)
        
        
#s = Solution()
#s.isMatch("aa", "a*a")
        
        
       
            
