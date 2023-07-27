#include<iostream>
#include<string>
#include<map>

typedef std::map<std::string, int> umap;
void printMap(umap myMap);

int main(){
	umap myMap;
	myMap["one"] = 1;
	myMap["two"] = 2;
	myMap["three"] = 3;

	printf("myMap.size(): %lu\n", myMap.size());
	printf("myMap.empty(): %d\n", myMap.empty());
	printMap(myMap);
	
	myMap.clear();
	printf("myMap.empty(): %d\n", myMap.empty());

	myMap["four"] = 4;
	printMap(myMap);
	myMap.erase("four");
	printMap(myMap);

}

// print given map
void printMap(umap myMap){
	umap::iterator itr;
	std::cout<<"printing map started\n";
	for(itr = myMap.begin(); itr != myMap.end(); itr++){
		std::cout<<"Key: "<<itr->first<<",\t Value: "<<itr->second<<"\n";
	}
	std::cout<<"printing map done\n";
}