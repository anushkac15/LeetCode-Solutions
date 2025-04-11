/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    int solve(TreeNode* root, int &diff){
        if(root==NULL){
            return 0;
        }

        int left = solve(root->left, diff);
        int right = solve(root->right,diff);

        diff = max(diff, abs(left-right));

        return 1+max(left, right);

    }
    
    bool isBalanced(TreeNode* root) {

        int diff =0;
        solve(root, diff);

        return diff>1 ?false:true;
                
    }
};