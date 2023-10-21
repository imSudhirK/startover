#include<iostream>
#include<string>
#include<unordered_map>
// array of characters with last character as null

// typedef: keyword, provides new name to existing data types
typedef long long int lli;
typedef std::string string;

// function declarations
string reverseLtoR(string str, int l, int r);
lli countSubStrDistChar(string str);
bool isShuffledSubStr(string A, string B);
int hammingDistance(string str1, string str2);
bool isPalindrome(string str);
char kthNonRepeatingChar(string str, int k);

int main(){
	string str = "geeksforgeeks";
	std::cout<<reverseLtoR(str, 3, 7)<<std::endl;
	std::cout<<countSubStrDistChar(str)<<std::endl;

	string B = "hello", A = "lhelo";
	std::cout<<isShuffledSubStr(A, B)<<std::endl;

	string binStr1= "10101010";
    string binStr2 = "01010101";
    std::cout<<hammingDistance(binStr1, binStr2)<<std::endl;

    string strpal = "abdcba";
    std::cout<<isPalindrome(strpal)<<std::endl;

    str = "geeksforgeeks";
    std::cout<<kthNonRepeatingChar(str, 3);
	return 0;
}
// functions definitions starts here

// reverse given string
string reverseLtoR(string str, int l, int r){
	while(l < r){
		char c = str[l];
		str[l] = str[r];
		str[r] = c;
		l++; r--;
	}
	return str;
}

// Count of substrings having all distinct characters
lli countSubStrDistChar(string str){
	int size = (int)str.size();
	lli ans = 0;
	int alpha[26];
	memset(alpha, 0, sizeof(alpha));
	
	int i = 0, j = 0;
	while(i < size){
		if(j < size && (alpha[str[j] - 'a']) == 0){
			ans += (j - i + 1);
			alpha[str[j] - 'a']++;
			j++;
		} else {
			alpha[str[i] - 'a']--;
			i++;
		}
	}

	return ans;
}

// Check if the given string is shuffled substring of another string
bool isShuffledSubStr(string A, string B){
	int la = A.length(), lb = B.length();
	if(la > lb) return false;
	sort(A.begin(), A.end());
	for(int i=0; i < lb; i++){
		if(la > lb - i) return false;
		string str = "";
		for(int j=i; j < i + la; j++) str += B[j];
		sort(str.begin(), str.end());
		if(str == A) return true;
	}
	return false;
}

// calculate hamming distance between two binary strings
int hammingDistance(string str1, string str2){
	int hamming = 0;
	for(int i=0; i < str1.length(); i++){
		if(str1[i] != str2[i]) hamming++;
	}

	return hamming;
}

// Check if a Given String is Palindrome
bool isPalindrome(string str){
	int i = 0, j = str.size() - 1;
	while(i < j){
		if(str[i] != str[j]) return false;
		i++; j--;
	}
	return true;
}

// K’th Non-repeating Character
char kthNonRepeatingChar(string str, int k){
	std::unordered_map<char, int> umap;
	for(int i=0; i < str.length(); i++){
		umap[str[i]]++;
	}

	int nrc = 0;
	for(int i=0; i< str.length(); i++){
		if(umap[str[i]] == 1){
			nrc++;
			if(nrc == k) return str[i];
		} else continue;
	}

	return '\0';
}
