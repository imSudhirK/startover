#include<iostream>
#include<vector>
using namespace std;

typedef vector<int> vi;

int minCost(vi & v){
	cout<<v.size();
	if(v.size() < 2) return 0;
	if(v.size() == 2) return min(v[0], v[1]);
	else return 100;
}

int main(){
	vi vec;
	vec.push_back(10); vec.push_back(15); 
	int res = minCost(vec);
	cout<<res;


}