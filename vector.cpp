#include<iostream>
#include<vector>

typedef std::vector<int> vi;

void printVector(vi myVec);
void printReverse(vi myVec);

int main(){
	vi myVec;
	myVec.assign(2, 5);
	myVec.push_back(0);
	myVec.push_back(1);
	myVec.push_back(2);
	myVec.push_back(3);
	printVector(myVec);
	printReverse(myVec);
	printf("myVec.size(): %lu\n", myVec.size());
	printf("myVec.front(): %d\n", myVec.front());
	printf("myVec.back(): %d\n", myVec.back());
	myVec.pop_back();
	printVector(myVec);

}

// print vector 
void printVector(vi myVec){
	std::cout<<"print vector:\t";
	for(vi::iterator itr = myVec.begin(); itr != myVec.end(); itr++){
		std::cout<<*itr<<" ";
	}
	std::cout<<std::endl;
}

// print vector in reverse order
void printReverse(vi myVec){
	std::cout<<"print reverse:\t";
	for(vi::reverse_iterator itr = myVec.rbegin(); itr != myVec.rend(); itr++){
		std::cout<<*itr<<" ";
	}
	std::cout<<std::endl;
}
