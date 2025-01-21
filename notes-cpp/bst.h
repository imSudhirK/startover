#ifndef BST_H
#define BST_H
// TODO
#include<iostream>

class TreeNode{
	int data;
	TreeNode* left;
	TreeNode* right;


	TreeNode(int val){
		this->data = val; 
		this->left = nullptr;
		this->right = nullptr;
	}
};

class binarySearchTree{
private:
	TreeNode* root;

	TreeNode* insert(TreeNode* node, int val){
		if(node == nullptr) return new TreeNode(val);
		if(val > node->data){
			node->right = insert(node->right, val);
		}else if(val < node->data){
			node->left = insert(node->left, val);
		}
		return node;
	}
};

#endif