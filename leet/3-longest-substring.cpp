#include<iostream>
#include<unordered_map>
using namespace std;

typedef unordered_map<char, int> mp;

int lengthOfLongestSubstring(string s){
    int leftInd = 0, maxLength = 0;
    mp umap;
    for(int ri = 0; ri < s.size(); ri++){
        if(umap.count(s[ri]) == 0 || umap[s[ri] < leftInd]){
            maxLength = max(maxLength, ri - leftInd + 1);
        }else{
            leftInd = umap[s[ri]] + 1;
        }
        umap[s[ri]] = ri;
    }
    return maxLength;
}

int main (){
    string s = "abcabcbb";
    cout<<lengthOfLongestSubstring(s)<<endl;
}