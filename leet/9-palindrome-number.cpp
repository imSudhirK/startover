#include<iostream>
#include<string>
using namespace std;

bool isPalindrome(int x){
    string s = to_string(x);
    for(int i = 0; i < s.size(); i++){
        if(s[i] != s[s.size() - 1 - i]){
            return false;
        }
    }
    return true;
}

bool isPalindromeV2(int x){
    if(x < 0) return false;
    if(x < 9) return true;
    int reverse = 0, original = x;
    while(x){
        reverse = reverse*10 + x%10;
        x = x/10;
    }
    return original == reverse;
}

int main(){
    int n;
    cout<<"Enter integer n: ";
    cin>>n;
    cout<<isPalindrome(n)<<endl;
    cout<<isPalindromeV2(n)<<endl;
}