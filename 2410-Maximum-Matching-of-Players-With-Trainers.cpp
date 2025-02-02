class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {

        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());

        int np = 0;
        int nt =0;

        while(np<players.size() && nt<trainers.size()){
            if(players[np]<= trainers[nt]){
                np++;
            }
            nt++;
        }
        return np;
    }
};