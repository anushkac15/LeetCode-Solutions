class Solution {
public:
    bool solve(string& s, int l, int r){
        if(l>=r){
            return true;
        }

        if(s[l]==s[r]){
            return solve(s, l+1, r-1);
        }

        return false;
    }
    string longestPalindrome(string s) {

        int n = s.size();
        int maxlen = 0;
        int start =0;

        for(int i =0;i<n;i++){
            for(int j =i;j<n;j++){
                if(solve(s,i,j) and j-i+1>maxlen){
                    maxlen = j-i+1;
                    start =i;
                }
            }
        }

        return s.substr(start, maxlen);
    }
};