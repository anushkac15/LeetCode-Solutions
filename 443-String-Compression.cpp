class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int index = 0; // Position to overwrite in chars

        for (int i = 0; i < n; ) {
            char currentChar = chars[i];
            int count = 0;

            // Count consecutive occurrences
            while (i < n && chars[i] == currentChar) {
                count++;
                i++;
            }

            // Store character
            chars[index++] = currentChar;

            // Store count (if greater than 1)
            if (count > 1) {
                for (char c : to_string(count)) {
                    chars[index++] = c;
                }
            }
        }

        return index; // New compressed size
    }
};
