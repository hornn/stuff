# https://leetcode.com/problems/guess-the-word/

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    
    @staticmethod
    def findOverlap(first, second):
        score = 0
        for first_letter, second_letter in zip(first, second):
            if first_letter == second_letter:
                score += 1
        return score
    
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        bads = []
        maybes = dict()
        goods = []
        for i in range(6):
            bads.append(set())
        
        # attempt 1 - sort wordlist?
        wordlist = sorted(wordlist)
            
        for word in wordlist:
            skip = False
            # check if word is eliminated:
            for idx, letter in enumerate(word):
                if letter in bads[idx]:
                    #print("%s is bad (bads: %s)" % (word, bads))
                    skip = True
                    continue
               
            for maybe_word, maybe_score in maybes.items():
                overlap = Solution.findOverlap(maybe_word, word)
                if overlap != maybe_score:
                    #print("skipping %s: overlap with %s (score %d) is %d" % (word, maybe_word, maybe_score, overlap))
                    skip = True
                    continue
            
            if skip:
                continue
         
            res = master.guess(word)
            print("guessed %s - score %d" % (word, res))
            if res <= 0:
                # eliminate all letters in this word
                for i in range(6):
                    bads[i].add(word[i]) 
            elif res == 6:
                print("found %s" % word)        
                return
            else:
                maybes[word] = res
                
