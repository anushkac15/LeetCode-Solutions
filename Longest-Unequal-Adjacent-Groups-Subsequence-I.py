class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        for i in range(len(groups)-2,-1,-1):
            if(groups[i]==groups[i+1]):
                del(words[i+1])
                del(groups[i+1])
        return words
        