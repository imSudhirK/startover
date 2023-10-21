#include<iostream>
#include<queue>

typedef std::queue<int> qi;

void printQueue(qi myqueue){
	while(!myqueue.empty()){
		std::cout<<myqueue.front()<<" ";
		myqueue.pop();
	}
	printf("\n");
}

int main(){

	qi myqueue;
	myqueue.push(0);
	myqueue.push(1);
	printf("myqueue.front(): %d\n", myqueue.front());
	printf("myqueue.back(): %d\n", myqueue.back());
	printf("myqueue.size(): %lu\n", myqueue.size());
	printQueue(myqueue);
	printQueue(myqueue);

	return 0;
}