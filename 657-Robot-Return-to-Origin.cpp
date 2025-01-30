class Solution {
public:
    bool judgeCircle(string moves) {

        int x =0;
        int y=0;

        for(char move: moves){
            if(move=='U'){
                y--;
            }
            else if(move=='R'){
                x++;
            }
            else if(move=='L'){
                x--;
            }
            else if(move=='D'){
                y++;
            }
        }

        return y==0 &&x==0;
        
    }
};