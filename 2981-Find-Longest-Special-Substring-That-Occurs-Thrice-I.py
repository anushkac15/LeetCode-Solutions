class Solution:
    def maximumLength(self, s: str) -> int:
        count = {}
        count_strings = 0
        for start in range(len(s)):
            character = s[start]
            substring_length = 0
            for end in range(start, len(s)):
                if character == s[end]:
                    substring_length += 1
                    count[(character, substring_length)] = (
                        count.get((character, substring_length), 0) + 1
                    )
                else:
                    break

        ans = 0
        for i in count.items():
            length = i[0][1]
            if i[1] >= 3 and length > ans:
                ans = length
        if ans == 0:
            return -1
        return ans