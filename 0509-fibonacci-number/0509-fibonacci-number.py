class Solution(object):
    def fib(self, n):
        
        if (n<=1):
            return n
        else:
            flast= self.fib(n-1)
            slast = self.fib(n-2)
            x=flast + slast
            return x

        
        