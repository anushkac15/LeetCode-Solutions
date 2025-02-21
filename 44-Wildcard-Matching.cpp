class Solution {
public:
    bool solve(int index1, int index2, string &text, string &pattern, vector<vector<int>> &dp) {
        if (index1 == text.size() && index2 == pattern.size()) return true;
        if (index2 == pattern.size() && index1 < text.size()) return false;
        if (index1 == text.size() && index2 < pattern.size()) {
            for (int i = index2; i < pattern.size(); i++) {
                if (pattern[i] != '*') return false;
            }
            return true;
        }
        if (dp[index1][index2] != -1) return dp[index1][index2];

        if (text[index1] == pattern[index2] || pattern[index2] == '?') {
            return dp[index1][index2] = solve(index1 + 1, index2 + 1, text, pattern, dp);
        }

        if (pattern[index2] == '*') {
            return dp[index1][index2] = solve(index1 + 1, index2, text, pattern, dp) || solve(index1, index2 + 1, text, pattern, dp);
        }

        return dp[index1][index2] = false;
    }

    bool isMatch(string s, string p) {
        int n1 = s.size();
        int n2 = p.size();
        vector<vector<int>> dp(n1 + 1, vector<int>(n2 + 1, -1));
        return solve(0, 0, s, p, dp);
    }
};
