class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {

        unordered_map<int,int> mp;
        int cnt =0;

        for(int i =0;i<nums.size();i++){
            cnt+= mp[nums[i]-k] +mp[nums[i]+k] ;
            mp[nums[i]]++;
        }

        return cnt;


        
    }
};