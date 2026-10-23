class Solution(object):
    def maximumProduct(self, nums):
        x= nums.sort()
        p=(nums[-1])*(nums[-2])*(nums[-3])
        p1=nums[0]*nums[1]*nums[-1]
        return max(p,p1)
        