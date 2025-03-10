class Solution {
public:
    void solve(int openP, int closeP, string s, int n, vector<string>& res) {
        if (openP == closeP && openP + closeP == n * 2) {
            res.push_back(s);
            return;
        }

        if (openP < n) {
            solve(openP + 1, closeP, s + \(\, n, res);
        }

        if (closeP < openP) {
            solve(openP, closeP + 1, s + \)\, n, res);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        solve(0, 0, \\, n, res);
        return res;        
    }
};