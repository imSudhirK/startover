#include<iostream>
#include<vector>
using namespace std;
typedef vector<int> vi;

/* leetcode 70 */
int climbStairsRec(int n){
    if(n < 3) return n;
    return climbStairsRec(n-1) + climbStairsRec(n-2);
}

int climbStairsDp(int n){
    if(n < 3) return n;
    vi ways(n + 1, 0);
    ways[1] = 1; ways[2] = 2;
    for(int i = 3; i < n + 1; i++){
        ways[i] = ways[i-1] + ways[i-2];
    }
    return ways[n];
}


int main(){
    int numStairs = 5;
    cout<<climbStairsRec(numStairs)<<endl;
    cout<<climbStairsDp(numStairs)<<endl;
}