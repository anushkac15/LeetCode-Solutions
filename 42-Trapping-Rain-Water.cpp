class Solution {
public:
    int trap(vector<int>& height) {

        int l = 0;
        int r = height.size() -1;

        int maxl = height[l];
        int maxr = height[r];

        int cnt =0;

        while(l<r){
            if(maxl<maxr){
                l+=1;
                maxl = max(maxl, height[l]);
                cnt+=maxl-height[l];
            }

            else{
                r-=1;
                maxr = max(maxr, height[r]);
                cnt+=maxr-height[r];
            }
        }
        

        return cnt;
    }
};