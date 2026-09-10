class Solution(object):
    def removeElement(self, nums, val):
        l=[]
        for i in nums:
            if i!=val:
                l.append(i)
        for i in range (len(l)):
            nums[i]=l[i]
        return len(l)

        
        