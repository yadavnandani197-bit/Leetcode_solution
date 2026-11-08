class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        for num in range(left, right + 1):
            is_self_dividing = True
            for digit_char in str(num):
                digit = int(digit_char)
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                result.append(num)
        return result
        