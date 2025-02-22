class Solution {
public:
    bool isIsomorphic(string s, string t) {

        unordered_map<char, int> mapS;
        unordered_map<char, int> mapT;

        for(int i =0;i< s.length();i++){
            if(mapS.find(s[i]) == mapS.end()){
                mapS[s[i]] = i;
            }
            if(mapT.find(t[i]) == mapT.end()){
                mapT[t[i]] = i;
            }

            if(mapS[s[i]] != mapT[t[i]]){
                return false;
            }
        }

        return true;
        
    }
};