#include<iostream>
// TODO
// recursive functions
int fibonacciR(int n);

// tail recursion

int main(){
	int n = 8;
	printf("fibonacciR(%d): %d\n", n, fibonacciR(n));
}

int fibonacciR(int n){
	if(n < 2) return n;
	return fibonacciR(n-1) + fibonacciR(n-2);
}
