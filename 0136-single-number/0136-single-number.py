class Solution(object):
    def singleNumber(self, nums):
        c=0
        for i in nums:
            c = c ^ i
        return c

        