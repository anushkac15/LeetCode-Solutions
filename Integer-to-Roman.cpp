class Solution {
public:
    string intToRoman(int num) {

        int number[] ={1,4,5,9,10,40,50,90,100,400,500,900,1000};
        string roman[] = {\I\,\IV\,\V\,\IX\,\X\,\XL\,\L\,\XC\,\C\,\CD\,\D\,\CM\,\M\};

        int i =12;
        string ans = \\;

        while(num>0){
            int div = num/number[i];
            num%=number[i];

            while(div--){
                ans+=roman[i];
            }

            i--;
        }

        return ans;    
    }
};