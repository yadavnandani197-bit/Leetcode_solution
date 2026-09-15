class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max=0
        c=0

        for n in nums:
            if n==1:
                c+=1
                if c>max:
                    max=c
            else:
                c=0
        return max
        