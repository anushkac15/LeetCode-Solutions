class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), [](const string& a, const string& b) {
            return a.size() < b.size();
        });
        
        unordered_map<string, int> dp;
        int longestChain = 1;

        for (string& word : words) {
            dp[word] = 1; 
            for (int i = 0; i < word.size(); ++i) {
                string predecessor = word.substr(0, i) + word.substr(i + 1);
                if (dp.find(predecessor) != dp.end()) {
                    dp[word] = max(dp[word], dp[predecessor] + 1);
                }
            }
            longestChain = max(longestChain, dp[word]);
        }

        return longestChain;
    }
};
