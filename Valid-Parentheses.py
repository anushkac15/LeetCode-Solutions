class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        mp = {\}\:\{\, \]\:\[\,\)\:\(\}

        for char in s:
            if char in mp.values():
                st.append(char)

            elif char in mp.keys():
                if not st or mp[char]!= st.pop():
                    return False

        return not st


        