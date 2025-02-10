class Solution {
public:

    int binarySearch(vector<int> & sorted, int target){

        int l = 0;
        int r = sorted.size();

        while(l<r){
            int mid = l+(r-l)/2;

            if(sorted[mid]<target){

                l = mid+1;
            }

            else{
                r= mid;
            }
        }

        return l;
    }

    int lengthOfLIS(vector<int>& nums) {

        int n = nums.size();
        vector<int> sorted;

        for(int i =0;i<n;i++){

            int index = binarySearch(sorted, nums[i]);

            if(index == sorted.size()){
                sorted.push_back(nums[i]);
            }
            else{
                sorted[index]= nums[i];
            }
        }
        return sorted.size();

        
    }
};