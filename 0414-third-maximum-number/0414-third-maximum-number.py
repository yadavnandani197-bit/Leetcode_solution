class Solution(object):
    def thirdMax(self, nums):
        first = second = third = float('-inf')

        for n in nums:
            if n == first or n == second or n == third:
                continue

            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n

        if third == float('-inf'):
            return first
        return third
        