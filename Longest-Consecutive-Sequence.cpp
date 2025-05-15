class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> st(nums.begin(),nums.end());

        int ans = 0;

        for(int num:st){
            if(st.find(num-1)==st.end()){
                int len =1;
                int n = num;

                while(st.find(n+1)!= st.end()){
                    n++;
                    len++;
                }

                ans = max(ans,len);
            }

        }

        return ans;
        
    }
};