class Solution(object):
    def moveZeroes(self, nums):
        x=0
        for y in range (len(nums)):
            if nums[y]!= 0:
                nums[x] , nums[y] = nums[y] , nums[x]
            
                x=x+1

