class Solution(object):
    def isSubsequence(self, s, t):
        x = 0
        for i in t:
            if x < len(s) and s[x] == i:
                x += 1
        return x == len(s)