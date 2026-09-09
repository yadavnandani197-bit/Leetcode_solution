class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        ca=0
        for i in nums:
            if c==0:
                ca=i
            if i ==ca:
                c = c+1
            else:
                c =c-1
        return ca