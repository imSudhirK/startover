#include<iostream>
// TODO
class TreeNode{
public:
    int data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val): data(val), left(nullptr), right(nullptr){}
};


class binarySearchTree{
private:
    TreeNode* root;
    
    TreeNode* insert(TreeNode* node, int val){
        if(node == nullptr) return new TreeNode(val);
        if(val < node->data){
            node->left = insert(node->left, val);
        }else if(val > node->data){
            node->right = insert(node->right, val);
        }
        return node;
    }

    void inOrder(TreeNode* node){
        if(node == nullptr) return;
        inOrder(node->left);
        std::cout<<node->data<<" ";
        inOrder(node->right);
    }

public:
    binarySearchTree(): root(nullptr){}

    void insertVal(int val){
        root = insert(root, val);
    }

    void inOrderTraversal(){
        inOrder(root);
        std::cout<<std::endl;
    }
};

int main(){
    binarySearchTree bst;
    bst.insertVal(5);
    bst.insertVal(3);
    bst.insertVal(7);
    bst.insertVal(2);
    bst.insertVal(4);

    bst.inOrderTraversal();

    std::cout<<"hello world!\n";
}