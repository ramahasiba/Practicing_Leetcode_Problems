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
    void helper(TreeNode* root, vector<int>&nodesValues){
        if(!root){
            return;
        }
        nodesValues.push_back(root->val);
        helper(root->left, nodesValues);
        helper(root->right, nodesValues);
    } 
    vector<int> preorderTraversal(TreeNode* root) { 
        vector<int> nodesValues;
        helper(root, nodesValues);
        return nodesValues;
    };
};