class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        n = min(len(word1), len(word2))
        for i in range(n):
            merged+=word1[i]+word2[i]
        
        merged+=word1[n:]+word2[n:]

        return merged