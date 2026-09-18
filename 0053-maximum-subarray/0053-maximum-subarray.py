class Solution(object):
    def maxSubArray(self, nums):
        total=0
        answer = nums[0]
        for i in nums:
            if total<0:
                total=0
            total = total + i
            if total>answer:
                answer = total
        return answer        