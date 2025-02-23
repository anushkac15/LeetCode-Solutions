class Solution {
public:
    bool isValid(string s) {
        stack<char> st;  

        for(char ch : s) {
            if(ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            }
            else {
                if(st.empty()) return false;

                char open = st.top();
                st.pop();

                if((ch == ')' && open != '(') || 
                   (ch == ']' && open != '[') || 
                   (ch == '}' && open != '{')) {
                    return false;
                }
            }
        }
        
        return st.empty();  
    }
};

