#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void) {
  int a[10001] = {};
  int b[10001] = {};
  int res[10002] = {};
  string input1, input2;
  
  cin >> input1 >> input2;
  
  for(int i = 0; i < input1.length(); i++) {
    a[i] = input1.at(input1.length() - i - 1) - '0';
  }
  
  for(int i = 0; i < input2.length(); i++) {
    b[i] = input2.at(input2.length() - i - 1) - '0';
  }
  
  int maxLen = max(input1.length(), input2.length());
  
  for (int i = 0; i < maxLen; i++) {
    if (res[i] + a[i] + b[i] >= 10) res[i + 1] = 1;
    res[i] = (res[i] + a[i] + b[i]) % 10;
  }
  
  if (res[maxLen] == 1) cout << 1;
  for (int i = maxLen - 1; i >= 0; i--) {
    cout << res[i];
  }
}