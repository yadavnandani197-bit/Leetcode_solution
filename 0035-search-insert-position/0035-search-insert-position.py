class Solution(object):
    def searchInsert(self, nums, target):
        c=-1
        for i in range(len(nums)):
            c=c+1
            if nums[i]==target or nums[i]>target:
                return i
        return len(nums)