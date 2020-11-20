# https://leetcode.com/problems/decode-string/
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #print("decodeString", s)
        if len(s) == 1:
            return s
        
        res = ''
        
        num = 0
        brackets_count = 0
        open_brackets = True
        text = ''
        inside_brackets = ''
        for letter in s:
            #print("LETTER", letter)
            
            if letter == ']':                
                brackets_count -= 1
                
            if brackets_count:
                text += letter
            
            elif letter.isdigit():
                num = num*10 + int(letter)
                #print("num", num)
            elif letter not in ['[', ']']:
                text += letter
                
            if letter == '[':
                brackets_count += 1
                
            if brackets_count == 0 and text:
                #print("text", text)
                inside_text = self.decodeString(text)
                #print("inside_text", inside_text)
                if num == 0:
                    num = 1
                res += inside_text * num
                num = 0
                text = ''
                #print("interim res", res)
        if text:
            inside_text = self.decodeString(text)
            #print("last inside_text", inside_text)
            res += inside_text * num
        #print("res", res)
        return res
