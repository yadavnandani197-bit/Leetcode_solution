class Solution(object):
    def reverseDegree(self, s):
        abc = "abcdefghijklmnopqrstuvwxyz"
        total = 0

        for i in range(len(s)):
            ch = s[i] 
            pos_in_string = i + 1 

            normal_pos = abc.index(ch) 
            reverse_val = 26 - normal_pos 

            total = total + reverse_val * pos_in_string

        return total
        