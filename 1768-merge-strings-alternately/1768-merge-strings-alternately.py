class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        j=0
        alt=[]
        while i<len(word1) and j<len (word2):
            alt.append(word1[i])
            alt.append(word2[j])
            i = i+1
            j = j+1
        alt.append(word1[i:])
        alt.append(word2[j:])
        return "".join(alt)
        