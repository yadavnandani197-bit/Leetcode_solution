class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in s.split():
            x=s.split()[::-1]
            return ' '.join(x)
        

