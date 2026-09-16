class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        l=len(nums)

        for i in range(l):
            if nums[i]!=i:
                return i
        return l


            