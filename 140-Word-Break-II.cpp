class Solution {
public:
    vector<string> wordBreakHelper(const string& s, int start, const unordered_set<string>& dict, unordered_map<int, vector<string>>& memo) {
        if (memo.find(start) != memo.end()) return memo[start];
        if (start == s.length()) return {\\};

        vector<string> validSubstr;
        
        for (int end = start + 1; end <= s.length(); ++end) {
            string prefix = s.substr(start, end - start);
            if (dict.find(prefix) != dict.end()) {
                vector<string> suffixes = wordBreakHelper(s, end, dict, memo);
                for (const string& suffix : suffixes) {
                    validSubstr.push_back(prefix + (suffix.empty() ? \\ : \ \) + suffix);
                }
            }
        }
        
        return memo[start] = validSubstr;
    }
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        unordered_map<int, vector<string>> memo;
        return wordBreakHelper(s, 0, dict, memo);
    }

};
