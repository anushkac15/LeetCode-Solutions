class Solution {
public:
    string minWindow(string s, string t) {  
        int m = s.length();
        int n = t.length();

        if (m < n) return \\;

        vector<int> hashArr(128, 0);
        for (int i = 0; i < n; i++) {
            hashArr[t[i]]++;
        }

        int l = 0, r = 0;
        int ct = 0;
        int minLen = INT_MAX;
        int sIndex = -1;

        while (r < m) {
            char rightChar = s[r];
            if (hashArr[rightChar] > 0) {
                ct++;
            }
            hashArr[rightChar]--;

            while (ct == n) {
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    sIndex = l;
                }

                char leftChar = s[l];
                hashArr[leftChar]++;
                if (hashArr[leftChar] > 0) {
                    ct--;
                }
                l++;
            }

            r++;
        }

        return sIndex == -1 ? \\ : s.substr(sIndex, minLen);
    }
};
