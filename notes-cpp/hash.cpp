#include<iostream>
#include<map>
#include<vector>
#include<unordered_map>

typedef std::vector<int> vi;

bool isSubset(int arr1[], int m, int arr2[], int n);
bool sortByVal(const std::pair<int, int>&a, const std::pair<int, int>&b);
vi sortByFrequency(int arr[], int n);
void printVector(vi myVec);


int main(){

	int arr[] = {1, 2, 3, 4, 5};
	int brr[] = {2, 4};
	int la = sizeof(arr)/sizeof(arr[0]), lb = sizeof(brr)/sizeof(brr[0]);
	
	printf("is brr subset of arr: %d\n", isSubset(arr, la, brr, lb));

	int crr[] = {2, 5, 2, 8, 5, 6, 8, 8};
	vi res;
	res  = sortByFrequency(crr, sizeof(crr)/sizeof(crr[0]));
	printVector(res);



	return 0;
}


// find whether an array is subset of another array
bool isSubset(int arr1[], int m, int arr2[], int n){
	std::map<int, int> frequency;
	for(int i = 0; i < m; i++){ frequency[arr1[i]]++;}
	for(int i = 0; i < n; i++){
		if(frequency[arr2[i]] > 0) {frequency[arr2[i]]--;}
		else return false;
	}
	return true;
}

// Used for sorting by frequency. And if frequency is same, then by appearance
bool sortByVal(const std::pair<int, int>&a, const std::pair<int, int>&b){
	if(a.second == b.second) return a.first < b.first;
	return a.second > b.second;
}

// Sort elements by frequency
vi sortByFrequency(int arr[], int n){
	std::unordered_map<int, int> umap;
	for(int i = 0; i < n; i++){
		umap[arr[i]]++;
	}

	std::vector<std::pair<int, int> > supVec;
	copy(umap.begin(), umap.end(), back_inserter(supVec));
	sort(supVec.begin(), supVec.end(), sortByVal);

	vi res;
	for(int i = 0; i < supVec.size(); i++){
		while(supVec[i].second--){
			res.push_back(supVec[i].first);
		}
	}

	return res;
}

// print vector 
void printVector(vi myVec){
	std::cout<<"printing vector:\t";
	for(int i = 0; i < myVec.size(); i++){
		std::cout<<myVec[i]<<" ";
	}
	std::cout<<std::endl;
}