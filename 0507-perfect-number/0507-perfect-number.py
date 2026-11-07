class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
            
        x = 1  # 1 is always a proper divisor
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                x += i
                if i != num // i:
                    x += num // i
                    
        return x == num
        