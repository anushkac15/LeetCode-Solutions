class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.length()!=t.length()){
            return false;
        }

        unordered_map<char,int> mp ;

        for(char &ch:s){
            mp[ch]+=1;
        }

        for(char &ch:t){
            if(mp.find(ch)==mp.end() || mp[ch]==0){
                return false;
            }

            mp[ch]-=1;
        }

        return true;
        
    }
};