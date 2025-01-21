#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

typedef vector<int> vi;

void printVector(vi v);
vi twoSum(vi nums, int target);


int main(){
    vi vec{2,7,11,15};
    vi res = twoSum(vec, 9);
    printVector(res);
}

void printVector(vi v){
    for(int i = 0 ; i < v.size(); i++) cout<<v[i]<<" ";
    cout<<endl;
}

vi twoSum(vi nums, int target){
    unordered_map<int, int> umap;
    for(int i = 0; i < nums.size(); i++){
        umap[nums[i]] = i;
    }
    vi v;
    for(int i = 0; i < nums.size(); i++){
        int leftOver = target - nums[i];
        if(umap.count(leftOver) && umap[leftOver] != i){
            v.assign({umap[leftOver], i});
        }
    }
    sort(v.begin(), v.end());
    return v;
}

