class Solution {
public:

    bool solve(string s, unordered_set<string>& DictSet, int i, vector<int>& dp){
        if(i== s.size()){
            return true;
        }

        if(DictSet.find(s)!= DictSet.end()){
            return true;
        }

        if(dp[i]!=-1){
            return dp[i];
        }

        for(int idx =1; idx<s.size(); idx++){
            string substr = s.substr(i, idx);
            if(DictSet.find(substr)!= DictSet.end() && solve(s, DictSet, i+idx, dp)){
                return dp[i]=true;
            }
        }

        return dp[i] = false;
    }
    bool wordBreak(string s, vector<string>& wordDict) {

        unordered_set<string> DictSet(wordDict.begin(), wordDict.end());
        vector<int> dp(s.size(), -1);

        return solve(s, DictSet, 0, dp);
        
    }
};