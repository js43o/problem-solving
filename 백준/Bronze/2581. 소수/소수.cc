#include <iostream>
using namespace std;

bool isPrime(int);

int main() {
	int n, m, l;
	bool isFirst = false;
	cin >> n >> m;
	
	int sum = 0;
	for (int i = n; i <= m; i++) {
		if (isPrime(i)) {
			if (!isFirst) {
				l = i;
				isFirst = true;
			}
			sum += i;
		}
	}
	
	if (sum == 0)
		cout << -1 << endl;
	else
		cout << sum << endl << l << endl;
}

bool isPrime(int n) {
	if (n == 1) return false;
	if (n == 2) return true;
	for (int i = 2; i < n; i++)
		if (n % i == 0) return false;
	return true;
}