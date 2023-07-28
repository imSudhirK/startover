#include<iostream>
#include "helper.cpp"
using namespace std;


void bubbleSort(int arr[], int n);
void selectionSort(int arr[], int n);
void insertionSort(int arr[], int n);


int main() {
	int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
	int n = sizeof(arr)/sizeof(arr[0]);
	printArray(arr, n);
	// bubbleSort(arr, n);
	// selectionSort(arr, n);
	insertionSort(arr, n);
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
