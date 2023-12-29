#include<iostream>
using namespace std;

typedef vector<int> vi;

int maxArea(vi height){
    int lh = height.size();
    if(lh < 2) return 0;
    int lptr = 0 , rptr = lh - 1, maxa = 0;
    while(lptr < rptr){
        if(height[lptr] <= height[rptr]){
            maxa = max(maxa, (rptr - lptr)*height[lptr]);
            lptr += 1;
        }else{
            maxa = max(maxa, (rptr - lptr)*height[rptr]);
            rptr -= 1;
        }
    }
    return maxa;
}

int main(){
    vi v{1,8,6,2,5,4,8,3,7};
    cout<<maxArea(v)<<endl;
}