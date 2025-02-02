class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        

        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int cookie = 0;
        int children =0;

        while(cookie<s.size() && children<g.size()){
            if(s[cookie] >= g[children]){
                children+=1;
            }
            cookie++;
        }

        return children;
    }
};