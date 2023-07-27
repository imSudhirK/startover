#include<iostream>
using namespace std;

bool linearSearch(int arr[], int n, int x);
bool binarySearchR(int arr[], int l, int r, int x);
bool binarySearchItr(int arr[], int l, int r, int x);

int main(){
	int arr[] = {0, 1, 2, 3, 4, 5, 6, 7};
	int la = sizeof(arr)/sizeof(arr[0]);

	printf("8 %s found in arr\n", linearSearch(arr, la, 8) ? "" : "not");
	printf("9 %s found in arr\n", binarySearchR(arr, 0, la-1, 9) ? "" : "not");
	printf("5 %s found in arr\n", binarySearchItr(arr, 0, la-1, 5) ? "" : "not");

}

// linear search algorithm
bool linearSearch(int arr[], int n, int x){
	for(int i = 0; i < n; i++){
		if(x == arr[i]) return true;
	}
	return false;
}

// binary search (recursive) algorithm for sorted array
bool binarySearchR(int arr[], int l, int r, int x){
	if(x == arr[l] || x == arr[r]) return true;
	if(l >= r) return false;
	int m = (l + r)/2;
	if(x == arr[m]) return true;
	if(x > arr[m]) return binarySearchR(arr, m+1, r, x);
	return binarySearchR(arr, l, m-1, x);
}

// binary search (iterative)
bool binarySearchItr(int arr[], int l, int r, int x){
	while(l <= r){
		int m = (l + r)/2;
		if(x == arr[m]) return true;
		if(x > arr[m]) l = m + 1;
		else r = m -1;
	}
	return false;
}