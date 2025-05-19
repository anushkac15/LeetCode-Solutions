class Solution {
public:
    string triangleType(vector<int>& nums) {

        sort(nums.begin(),nums.end());
        unordered_set<int> st(nums.begin(),nums.end());

        if(nums[0]+nums[1]<=nums[2]){
            return "none";
        }
        else if(st.size()==1){
            return "equilateral";
        }
        else if(st.size()==2){
            return "isosceles";
        }
        return "scalene";
        
    }
};