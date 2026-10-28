class Solution(object):
    def arrangeCoins(self, n):
        r=1
        while n>= r:
            n=n-r
            r=r+1
        return r-1
        