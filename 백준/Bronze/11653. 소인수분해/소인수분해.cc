#include <iostream>
#include <cmath>

using namespace std;

int isPrime(int n) {
  if (n == 2 || n == 3 || n % 2 == 0 || n % 3 == 0) return true;
  for (int i = n; i < sqrt(n); i++) {
    if (n % i == 0) return false;
  }
  return true;
}

int main(void) {
  int input;
  int p = 2;
  cin >> input;
  
  if (input == 1) return 0;
  
  while (p < input) {
    if (isPrime(p) && input % p == 0) {
      input = input / p;
      cout << p << endl;
    } else {
      p++;
    }
  }
  cout << p << endl;
}