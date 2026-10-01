class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=s.split()
        y=len(x[-1])
        return y
        