#include<iostream>
using namespace std;

typedef vector<string> vs;

string getPrefix(string s, string t){
    int ml = min(s.size(), t.size());
    while(ml){
        string ss = s.substr(0, ml);
        string st = t.substr(0, ml);
        if(ss == st) return ss;
        ml -= 1;
    }
    return "";
}

string longestCommonPrefix(vs strs){
    int ls = strs.size();
    if(ls < 1) return "";
    string prefix = strs[0];
    for(int i = 0; i < ls; i++){
        prefix = getPrefix(prefix, strs[i]);
    }
    return prefix;
}

int main(){
    vs v{"flower","flow","flight"};
    cout<<longestCommonPrefix(v)<<endl;
    return 0;
}