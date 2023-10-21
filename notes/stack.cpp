#include<iostream>
#include<stack>

typedef std::stack<int> sti;

void printStack(sti mystack){
	while(!mystack.empty()){
		std::cout<<mystack.top()<<" ";
		mystack.pop();
	}
	std::cout<<std::endl;
}

int main(){
	sti mystack;
	mystack.push(0);
	mystack.push(1);

	printf("top of mystack is: %d\n", mystack.top());
	printf("size of mystack is: %zu\n", mystack.size());
	printStack(mystack);

	return 0;
}