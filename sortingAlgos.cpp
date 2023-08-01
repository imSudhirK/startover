#include<iostream>
#include "helper.cpp"
using namespace std;


void bubbleSort(int arr[], int n);
void selectionSort(int arr[], int n);
void insertionSort(int arr[], int n);

int partitionArr(int arr[], int low, int high);
void quickSort(int arr[], int low, int high);

void mergeArr(int arr[], int left, int mid, int right);
void mergeSort(int arr[], int begin, int end);


int main() {
	int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
	int n = sizeof(arr)/sizeof(arr[0]);
	printArray(arr, n);
	// bubbleSort(arr, n);
	// selectionSort(arr, n);
	// insertionSort(arr, n);
	// quickSort(arr, 0, n-1);
	mergeSort(arr, 0, n-1);
	printArray(arr, n);


}

// sort array same as we remove bubbles from some packed item
void bubbleSort(int arr[], int n){
	for(int i = n-1; i > 0; i--){
		for(int j = 0; j < i; j++){
			if(arr[j] > arr[j+1]){
				swapVals(&arr[j], &arr[j+1]);
			}
		}
	}
}

// select minimum or maximum of unsorted portion and put at correct position
void selectionSort(int arr[], int n){
	for(int i = 0; i < n-1; i++){
		int min_ind = i;
		for(int j = i; j < n; j++){
			if(arr[j] < arr[min_ind]) min_ind = j;
		}
		if(min_ind != i) swapVals(&arr[i], &arr[min_ind]);
	}
}

// take from unsorted portion and insert at correct position of sorted portion
void insertionSort(int arr[], int n){
	for(int i = 1; i < n; i++){
		for(int j = i-1; j >= 0 && arr[j] > arr[j+1]; j--){
			swapVals(&arr[j], &arr[j+1]);
		}
	}
}

// takes pivot (last element) and places smaller to left and greater to right of pivot
int partitionArr(int arr[], int low, int high){
	int pivot = arr[high];
	int partitioningIndex = low;
	for(int j = low; j <= high - 1; j++){
		if(arr[j] >= pivot) continue;
		if(j != partitioningIndex) swapVals(&arr[j], &arr[partitioningIndex]);
		partitioningIndex++;
	}
	swapVals(&arr[high], &arr[partitioningIndex]);
	return partitioningIndex;
}

// quick sort,  time: O(n log n), space: O(1)
void quickSort(int arr[], int low, int high){
	if(low >= high) return;
	int partitioningIndex = partitionArr(arr, low, high);
	quickSort(arr, low, partitioningIndex - 1);
	quickSort(arr, partitioningIndex + 1, high);
}

// merges two subarrays of array
void mergeArr(int arr[], int begin, int mid, int end){
	int lenLeftArr = mid - begin + 1;
	int lenRightArr = end - mid;
	int *leftArr = new int[lenLeftArr], *rightArr = new int[lenRightArr];
	for(int i = 0; i < lenLeftArr; i++) leftArr[i] = arr[begin + i];
	for(int i = 0; i < lenRightArr; i++) rightArr[i] = arr[mid + 1 + i];
	int indLeftArr = 0, indRightArr = 0, indMergedArr = begin;
	while(indLeftArr < lenLeftArr && indRightArr < lenRightArr){
		if(leftArr[indLeftArr] > rightArr[indRightArr]){
			arr[indMergedArr] = rightArr[indRightArr];
			indRightArr++;
		} else {
			arr[indMergedArr] = leftArr[indLeftArr];
			indLeftArr++;
		}
		indMergedArr++;
	}
	while(indLeftArr < lenLeftArr){
		arr[indMergedArr] = leftArr[indLeftArr];
		indLeftArr++;
		indMergedArr++;
	}
	while(indRightArr < lenRightArr){
		arr[indMergedArr] = rightArr[indRightArr];
		indRightArr++;
		indMergedArr++;
	}
	delete[] leftArr;
	delete[] rightArr;
}

// merge sort, time: O(n log n); space: O(n)
void mergeSort(int arr[], int begin, int end){
	if(begin >= end) return;
	int mid = (begin + end)/2;
	mergeSort(arr, begin, mid);
	mergeSort(arr, mid + 1, end);
	mergeArr(arr, begin, mid, end);
}