class Solution(object):
    def maxPalindromes(self, s, k):
        n=len(s)

        ispal=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i <=2 or ispal[i+1][j-1]):
                    ispal[i][j]=True

        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            dp[i] = dp[i+1]
            
            for j in range (i+k-1,n):
                if ispal[i][j]:
                    dp[i]=max(dp[i], 1+dp[j+1])
                    break
        return dp[0]