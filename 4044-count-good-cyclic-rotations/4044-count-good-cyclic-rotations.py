class Solution(object):
    def countGoodRotations(self, nums):
        n= len(nums)
        half = n//2
        s= sum(nums)

        b= nums + nums
        cur = sum(b[:half])
        ans =0
        if 2*cur > s:
            ans +=1

        for i in range(1,n):
            cur += b[i+half-1] - b[i-1]
            if 2*cur > s:
                ans += 1
        return ans
        