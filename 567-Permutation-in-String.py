class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        matches = 0
        s1_len = len(s1)
        s1_dic = {}
        s2_dic = {}

        for char in s1:
            if char in s1_dic:
                s1_dic[char] += 1
            else:
                s1_dic[char] = 1
        
        left = 0 
        
        for i in range(len(s2)):

            if s2[i] in s2_dic:
                s2_dic[s2[i]] += 1
            else:
                s2_dic[s2[i]] = 1
                  
            if s2[i] in s1_dic:
                matches += 1
            
            if i + 1 - left > s1_len:
             
                if s2[left] in s1_dic:
                    matches -= 1
                
                if s2_dic[s2[left]] == 1:
                    del s2_dic[s2[left]]
                else:
                    s2_dic[s2[left]] -= 1
                
                left += 1
            
            if matches == s1_len and s1_dic == s2_dic:
                return True
            
        return False
                