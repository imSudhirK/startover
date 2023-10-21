#include<iostream>

// define typename using template
template <typename T>
void printArray(T arr[], int n){
	std::cout<<"printing arr: \t";
	for(int i = 0; i < n; i++){
		std::cout<<arr[i]<<" ";
	}
	std::cout<<"\n";
}

// keyword typename could be replaces with class
template <class T>
void swapVals(T* x, T*y){
	T temp = *x;
	*x = *y;
	*y = temp;
}

// its better to keep default typename at last
template <int maximum, typename U, typename T = int>
void printTTimes(U v, T t){
	T mx = std::min((T)maximum, t);
	std::cout<<"printing "<<v<<" "<<mx<<" times: \t";
	for(T i = 0; i < mx; i++){
		std::cout<<v;
	}
	std::cout<<"\n";
}


int main(){
	int arr[] = {1, 2, 3, 4, 5, 6, 7};
	int la = sizeof(arr)/sizeof(arr[0]);

	// typename could be skipped in upgraded compilers
	printArray<int>(arr, la);
	printArray(arr, la);
	printTTimes<5, char, float>('c', 200);

	double x1 = 20, x2 = 30;
	swapVals(&x1, &x2);
	std::cout<<"x1: "<<x1<<"\tx2: "<<x2<<std::endl;

}