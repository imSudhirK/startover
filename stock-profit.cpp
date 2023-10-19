#include<iostream>
#include<vector>
using namespace std;

typedef vector<int> vi;

/* leetcode 121 */
int maxProfit(vi prices){
    int lp = prices.size();
    if(lp <= 1) return 0;
    int maxp = max(0, prices[1] - prices[0]), currp = 0;
    for(int i = 1; i < lp; i++){
        if(currp <=0) currp = prices[i] - prices[i-1];
        else currp += prices[i] - prices[i-1];
        maxp = max(maxp, currp);
    }
    return maxp;
}

int main(){
    vi prices{7,1,5,3,6,4};
    cout<<maxProfit(prices)<<"\n";
}