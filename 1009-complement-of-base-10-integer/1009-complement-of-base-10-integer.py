class Solution(object):
    def bitwiseComplement(self, n):
        binary = bin(n)[2:]
        x = ""
        for i in binary:
            if i == "1":
                x += "0"
            else:
                x += "1"
        return int(x, 2)
        
        