#include<iostream>

struct Node {
	int data;
	struct Node* next;
};

void printLinkedList(struct Node* node);
int findLength(struct Node* node);
bool searchValue(Node* node, int val);
void pushFront(Node** head_ref, int val);
void insertAfter(Node* prev_node, int val);
void appendEnd(Node** head_ref, int val);
void reverseLinkedList(Node** head_ref);
void deleteNodeAtPosition(Node** head_ref, int pos);
bool detectLoop(Node* node);

int main(){
	struct Node* head = NULL;
	struct Node* second = NULL;

	head = (struct Node*)malloc(sizeof(struct Node));
	(*head).data = 1;

	second = (struct Node*)malloc(sizeof(struct Node));
	second->data = 2;

	(*head).next = second;

	struct Node* third = new Node();
	third->data = 3;

	second->next = third;

	printLinkedList(head);

	std::cout<<findLength(head)<<std::endl;
	searchValue(head, 3) ? std::cout<<"Yes, 3 exists\n" : std::cout<<"No, 3 doesn't exists\n";

	pushFront(&head, 0);
	printLinkedList(head);

	insertAfter(head->next->next, 4);
	printLinkedList(head);

	appendEnd(&head, 5);
	printLinkedList(head);

	reverseLinkedList(&head);
	printLinkedList(head);

	deleteNodeAtPosition(&head, 1);
	printLinkedList(head);

	std::cout<<detectLoop(head)<<std::endl;

	return 0;
}

// print linekd List
void printLinkedList(struct Node* node){
	while(node != NULL){
		printf("%d  ", (*node).data);
		node = (*node).next;
	}
	std::cout<<std::endl;
}

// find length of liked list
int findLength(Node* node){
	int len = 0;
	while(node){
		node = node->next;
		len++;
	}
	return len;
}

// search if val exists in linked list
bool searchValue(Node* node, int val){
	while(node != NULL){
		if(node->data == val) return true;
		node = node->next;
	}
	return false;
}

// push new node to the front of list
void pushFront(Node** head_ref, int val){
	Node* newNode = new Node();
	newNode->data = val;
	newNode->next = (*head_ref);
	(*head_ref) = newNode;
}

// insert new node after given node
void insertAfter(Node* prev_node, int val){
	if(prev_node == NULL){
		std::cout<<"given node could not be empty\n";
		return;
	}
	Node* newNode = new Node();
	(*newNode).data = val;
	newNode->next = prev_node->next;
	prev_node->next = newNode;
}

// append new node at end of linked list
void appendEnd(Node** head_ref, int val){
	Node* newNode = new Node();
	newNode->data = val;
	newNode->next = NULL;
	if(*head_ref == NULL){
		*head_ref = newNode;
		return;
	}
	Node* lastNode = *head_ref;
	while(lastNode->next != NULL){
		lastNode = lastNode->next;
	}
	lastNode->next = newNode;
}

// reverse the linked list
void reverseLinkedList(Node** head_ref){
	if((*head_ref) == NULL || (*head_ref)->next == NULL) return;
	Node *prevNode = NULL, *currNode = *head_ref, *nextNode = NULL;
	while(currNode != NULL){
		nextNode = currNode->next;
		currNode->next = prevNode;
		prevNode = currNode;
		currNode = nextNode;
	}
	(*head_ref) = prevNode;
}

// delete a linked list node at given position
void deleteNodeAtPosition(Node** head_ref, int pos){
	if((*head_ref) == NULL || pos < 0) return;
	Node* temp = *head_ref;
	if(pos == 0){
		*head_ref = (*head_ref)->next;
		free(temp);
		return;
	}
	while(temp && pos-1){
		temp = temp->next;
		pos--;
	}
	if(!temp) return;
	Node* nextNode = temp->next->next;
	free(temp->next);
	temp->next = nextNode;
}


// detect loop or cycle in a linked list
bool detectLoop(Node* node){
	if(node == NULL || node->next == NULL) return false;
	Node *fastPtr = node->next->next, *slowPtr = node;
	while(fastPtr && fastPtr != slowPtr){
		fastPtr = fastPtr->next;
		if(!fastPtr) return false;
		fastPtr = fastPtr->next;
		slowPtr = slowPtr->next;
	}
	if(!fastPtr) return false;
	return true;
} 
