// print array 
void printArray(int arr[], int n){
	std::cout<<"arr:\t";
	for(int i = 0; i < n; i++) std::cout<<arr[i]<<" ";
	std::cout<<"\n";
}

// swap values by reference
void swapVals(int* xp, int* yp){
	int temp = *yp;
	*yp = *xp;
	*xp = temp;
}