/* leet code 169 */
#include<iostream>
#include<vector>
using namespace std;

typedef vector<int> vi;

void printVector(vi v){
    for(int i = 0; i < v.size(); i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

int majorityElement(vi & v){
    int lv = v.size();
    if(lv == 1) return v[0];
    int mi = 0, c = 1;
    for(int i = 1; i < lv; i++){
        if(v[i] == v[mi]) c += 1;
        else c -= 1;
        if(!c){
            mi = i;
            c = 1;
        }
    }
    return v[mi];
}

int main(){
    vi vec{ 2,2,1,1,1,2,2 };
    cout<<majorityElement(vec)<<endl;
}

