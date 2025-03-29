class Solution {
public:

    void solve(string s, unordered_set<string>&DictSet,vector<string>& res, string ans, int i){
        if(i>=s.size()){
            res.push_back(ans);
            return;
        }

        for(int j =i;j<s.size();j++){
            string substr = s.substr(i, j-i+1);

            if(DictSet.find(substr) != DictSet.end()){

                string temp = ans;

                if(!ans.empty()){
                    ans+=\ \;
                }
                
                ans+=substr;

                solve(s, DictSet, res, ans, j+1);

                ans = temp;
            }
        }
    }
    vector<string> wordBreak(string s, vector<string>& wordDict) {

        unordered_set<string>DictSet(wordDict.begin(), wordDict.end());
        vector<string>res;
        string ans =\\ ;

        solve(s, DictSet, res, ans, 0);
        return res;

        
    }
};