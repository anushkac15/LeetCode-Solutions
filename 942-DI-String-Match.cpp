class Solution {
public:
    vector<int> diStringMatch(string s) {


        vector<int> ans;
        stack<int> cnt;

        for(int i =0;i<= s.length();i++){
            cnt.push(i);

            if(i== s.length() || s[i]=='I'){
                while(!cnt.empty()){
                    ans.push_back(cnt.top());
                    cnt.pop();

                }
            }
        }

        return ans;

        
    }
};