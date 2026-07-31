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
    int recurr(TreeNode* node, int d){
        if (!node){
            return d;
        }
        return std::max(recurr(node->left,d+1),recurr(node->right,d+1));
    }
    int maxDepth(TreeNode* root) {
        return recurr(root,0);
    }
};
