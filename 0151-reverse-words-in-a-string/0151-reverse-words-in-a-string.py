class Solution(object):
    def reverseWords(self, s):
        for i in s.split():
            x=s.split()[::-1]
            return ' '.join(x)
        

