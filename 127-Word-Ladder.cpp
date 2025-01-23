class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> bank(wordList.begin(), wordList.end());
        unordered_set<string> visited;

        queue<string> que;

        visited.insert(beginWord);
        que.push(beginWord);

        int level =0;

        while (!que.empty()){
            int n = que.size();

            while(n--){
                string curr = que.front();
                que.pop();

                if(curr==endWord){
                    return level+1;
                }

                for(char ch = 'a' ; ch<='z'; ch++){
                    for(int i =0;i<curr.size();i++){
                        string neighbour = curr;
                        neighbour[i] = ch;

                        if(visited.find(neighbour) == visited.end() && bank.find(neighbour) != bank.end()){
                            visited.insert(neighbour);
                            que.push(neighbour);
                        }
                    }
                }
            }
            level++;
        }
        return 0;
        
    }
};