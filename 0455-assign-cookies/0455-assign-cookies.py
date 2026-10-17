class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        c=0
        i=0
        for co in s:
            if i<len (g) and co>= g[i]:
                c=c+1
                i=i+1
        return c




        