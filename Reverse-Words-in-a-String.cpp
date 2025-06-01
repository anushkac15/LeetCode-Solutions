class Solution {
public:
    void reverseWord(string &s, int i, int j) {
        while (i < j) {
            swap(s[i], s[j]);
            i++;
            j--;
        }
    }

    string reverseWords(string &s) {
        int n = s.size();

        int i = 0, j = 0;
        while (j < n) {
            while (j < n && s[j] == ' ') j++;

            while (j < n && s[j] != ' ') {
                s[i++] = s[j++];
            }

            while (j < n && s[j] == ' ') j++;

            if (j < n) s[i++] = ' ';
        }

        s.resize(i);

        reverse(s.begin(), s.end());

        int start = 0;
        for (int k = 0; k <= s.size(); ++k) {
            if (k == s.size() || s[k] == ' ') {
                reverseWord(s, start, k - 1);
                start = k + 1;
            }
        }

        return s;
    }
};
