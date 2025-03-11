class Solution {
public:

    bool isVowel(char ch){
        return ch == 'a' || ch == 'e' || ch=='i' || ch=='o' || ch=='u';
    }

    long long countVowels(string word) {

        long long cnt =0;
        int n = word.length();

        for(int j = 0;j<n;j++){

            if(isVowel(word[j])){
                cnt += long(n-j) * long(j+1);
            }
        }

        return cnt;

    }
};