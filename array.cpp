#include<iostream>


void printArr(int arr[], int size);
void reverseArr(int arr[], int size);
void rotateArrClockwiseByOne(int arr[], int size);
int kadaneAlgo(int arr[], int size);
void dutchNationalFlag(int arr[], int size);
void swapArrVals(int arr[], int x, int y);

int main(){
	int n;
	std::cout<<"enter size of array:\n";
	std::cin>>n;

	int arr[n];
	std::cout<<"Enter elements of array:\n";
	for(int i=0; i<n; i++) std::cin>>arr[i];

	std::cout<<"input array is:\n";
	printArr(arr, n);

	reverseArr(arr, n);
	std::cout<<"array after reversing:\n";
	printArr(arr, n);

	rotateArrClockwiseByOne(arr, n);
	std::cout<<"array after rotating clockwise bu one:\n";
	printArr(arr, n);

	printf("maxium sum of contiguous subarray: %d\n", kadaneAlgo(arr, n));

	// dutch national flag's problem 
	// sort array containing only 0s, 1s and 2s
	int dutchArr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
	int s = sizeof(dutchArr)/sizeof(dutchArr[0]);
	printArr(dutchArr, s);
	dutchNationalFlag(dutchArr, s);
	std::cout<<"given dutch arr after sorting:\n";
	printArr(dutchArr, s);

	return 0;
}

void printArr(int arr[], int size){
	for(int i=0; i<size; i++){
		printf("%d\t", arr[i]);
	}
	printf("\n");
	return;
}

void reverseArr(int arr[], int size){
	for(int i=0; i<size/2; i++){
		int temp = arr[i];
		arr[i] = arr[size-1-i];
		arr[size-1-i] = temp;
	}
	return;
}

void rotateArrClockwiseByOne(int arr[], int size){
	int temp = arr[size-1];
	for(int i=size-1; i>0; i--) arr[i] = arr[i-1];
	arr[0] = temp;
	return;
}

int kadaneAlgo(int arr[], int size){
	int maxSoFar = 0, currMax = 0;
	for(int i=0; i<size; i++){
		currMax +=arr[i];
		if(maxSoFar < currMax) maxSoFar = currMax;
		if(currMax < 0) currMax = 0;
	}
	return maxSoFar;
}

void dutchNationalFlag(int arr[], int size){
	int lo = 0, md = 0, hi = size-1;
	// int temp;
	while(md <= hi){
		switch(arr[md]){
		case 0:
			swapArrVals(arr, md++, lo++);
			break;
		case 1:
			md++;
			break;
		case 2:
			swapArrVals(arr, md, hi--);
			break;
		}
	}
	return;
}

void swapArrVals(int arr[], int x, int y){
	int temp = arr[x];
	arr[x] = arr[y];
	arr[y] = temp;
	return;
}