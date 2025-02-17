class Solution {
public:

    void solve(string& tiles, vector<bool>& used, unordered_set<string>& res, string& curr){

        res.insert(curr);

        for(int i =0;i<tiles.size();i++){
            if(used[i]){
                continue;
            }

            used[i]=true;
            curr.push_back(tiles[i]);
            solve(tiles, used, res, curr);

            used[i] = false;

            curr.pop_back();


        }

        
    }


    int numTilePossibilities(string tiles) {

        unordered_set<string> res;

        vector<bool> used(tiles.length(), false);

        string curr ="";

        solve(tiles, used,res, curr);

        return res.size()-1;



        
    }
};