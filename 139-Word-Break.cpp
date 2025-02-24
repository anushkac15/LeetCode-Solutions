class Solution {
public:
    bool solve(string& s, unordered_set<string>& wordDict, vector<int>& memo, int i) {
        if (i == s.size()) return true;
        if (memo[i] != -1) return memo[i];

        for (const string& w : wordDict) {
            int len = w.length();
            if (i + len <= s.size() && s.substr(i, len) == w && solve(s, wordDict, memo, i + len)) {
                return memo[i] = true;
            }
        }

        return memo[i] = false;
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<int> memo(s.size(), -1);
        return solve(s, wordSet, memo, 0);
    }
};
