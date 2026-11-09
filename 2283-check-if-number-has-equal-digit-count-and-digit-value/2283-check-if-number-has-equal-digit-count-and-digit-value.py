class Solution(object):
    def digitCount(self, num):
        for i in range (len(num)):
            c=num.count(str(i))
            ex=int(num[i])
            if c != ex:
                return False
        return True
        