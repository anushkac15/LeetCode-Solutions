class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> adj[numCourses]; 
        vector<int> indegree(numCourses, 0);

        for(int i =0;i<prerequisites.size();i++){
            int first = prerequisites[i][0];
            int second = prerequisites[i][1];
            adj[second].push_back(first);
            indegree[first]++;
        }


        queue<int> que;

        for(int i =0;i<numCourses;i++){
            if(indegree[i]==0){
                que.push(i);
            }
        }

        vector<int> res;

        while(!que.empty()){
            int u = que.front();
            que.pop();
            res.push_back(u);

            for(int& v: adj[u]){
                indegree[v]--;

                if(indegree[v]==0){
                    que.push(v);
                }
            }
        }

        if(res.size() != numCourses){
            return {};
        }
        return res;
    }
};