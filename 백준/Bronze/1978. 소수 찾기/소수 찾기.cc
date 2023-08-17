#include <iostream>
using namespace std;

bool isPrime(int);

int main() {
	int n, input;
	cin >> n;
	int num[n] = {};
	for (int i = 0; i < n; i++) {
		cin >> input;
		num[i] = input;
	}
	int count = 0;
	for (int i = 0; i < n; i++)
		if (isPrime(num[i])) count++;
	cout << count << endl;
}

bool isPrime(int n) {
	if (n == 1) return false;
	if (n == 2) return true;
	for (int i = 2; i < n; i++)
		if (n % i == 0) return false;
	return true;
}