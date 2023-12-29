#include<iostream>
#include<string>
// using namespace std;

// & ampersand: address of operator
// * star: dereferencing operator
enum designation { SDE1, SDE2, SDE3, TechLead };

struct employee {
	std::string name;
	int salary;
	designation jobTitle;
};

int fibonacciRecursive(int n);
int fibonacciDynamic(int n);

int  wrapperFun( int (*funptr[])(int), int ind, int num){
	return funptr[ind](num);
}

int main(){

	/////////1. Integer pointers
	// declare and define a var with name: var, value: 10
	// it is allocated some address: say 0x16ae6f648
	int var = 10;
	// declare a pointer variable name: ptr, type int*
	// it is allocated another address: say 0x14abe2f544
	int *ptr; // integer pointer, pointer to integer
	// assign value as address of var, ptr: stores address of var
	ptr = &var;

	printf("ptr: %p,\tvar: %d,\t*ptr: %d\n", ptr, var, *ptr);

	// array name is pointer to its first element
	int arr[] = {1, 2, 3, 4, 5};
	int *arrPtr = arr;
	printf("arr: %p,\tarr[0]: %d\n", arr, arr[0]);
	printf("arrPtr: %p,\t*arrpt: %d\n", arrPtr, *arrPtr);

	////////2. Array pointers
	// pointer to arr of 5 intergers
	int (*ptrArr)[5];
	ptrArr = &arr;
	printf("arrPtr: %p,\tptrArr: %p\n", arrPtr, ptrArr);
	printf("*ptrArr:%p,\t**ptrArr:%d\n", *ptrArr, **ptrArr);
	// pointer arithmetic, it increases by size
	arrPtr++; ptrArr++;
	printf("arrPtr++: %p,\tptrArr++: %p\n", arrPtr, ptrArr);
	printf("*arr: %d,\t*(arr+1): %d\n", *arr, *(arr+1));

	int arr2d[][3] = {{1,2,3}, {4, 5, 6}, {7, 8, 9}};
	// arr2d: pointer to whole 0th row array(0 indexed)
	// *(arr2d+1): pointer to 0th element of 1st row
	// **(arr2d+1): value of 0th element of 1st row
	printf("arr2d: %p,\t**(arr2d+1): %d\n", arr2d, **(arr2d+1));

	/////////3. Structure pointer
	struct employee emp0;
	emp0.name = "sudhir"; emp0.salary = 14; emp0.jobTitle = SDE3;
	printf("emp0\t name:%s, \tsalary:%d\n", emp0.name.c_str(), emp0.salary);
	std::cout<<"emp0 jobTitle\t"<<emp0.jobTitle<<std::endl;

	employee emp1 = {"arvind", 12};
	std::cout<<"emp1 name: "<<emp1.name<<",\t salary: "<<emp1.salary<<"\n";

	employee* emp1Ptr = &emp1;
	std::cout<<"emp1 (*emp1Ptr).name: "<<(*emp1Ptr).name<<",\t(*emp1Ptr).salary: "<<(*emp1Ptr).salary<<"\n";
	std::cout<<"emp1 emp1Ptr->.name: "<<emp1Ptr->name<<",\temp1Ptr->salary: "<<emp1Ptr->salary<<"\n";

	//////////4. Function pointers
	// points to the code not data 
	int (*funPtr)(int) = &fibonacciRecursive;
	printf("(*funPtr)(8): %d,\tfunPtr(8): %d\n", (*funPtr)(8), (*funPtr)(8));
	// function name can also be used to get functions address
	int (*funPtr2)(int) = fibonacciRecursive;
	printf("(*funPtr2)(8): %d,\tfunPtr2(8): %d\n", (*funPtr2)(8), (*funPtr2)(8));

	// array of function pointers
	int (*funPtrs[])(int) = {fibonacciRecursive, fibonacciDynamic};
	int ch = 1; printf("funPtrs[1](8): %d\n", funPtrs[ch](8));
	// function pointers can be passed as argument and return from funtion
	printf("wrapperFun(funPtrs, 1, 8): %d\n", wrapperFun(funPtrs, 1, 8));

	return 0;
}

int fibonacciRecursive(int n){
	if(n < 2) return n;
	return fibonacciRecursive(n-2) + fibonacciRecursive(n-1);
}

int fibonacciDynamic(int n){
	if(n < 2) return n;
	int val = 0, ans = 1;
	for(int i = 2; i <= n; i++){
		int temp = ans;
		ans += val;
		val = temp;
	}
	return ans;
}