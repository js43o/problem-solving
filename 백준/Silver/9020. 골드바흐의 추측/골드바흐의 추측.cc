#include <iostream>
using namespace std;

bool isPrime(int n) {
	if (n == 1) return false;
	if (n == 2 || n == 3) return true;
	if (n % 2 == 0 || n % 3 == 0) return false;
	
	for (int i = 3; i * i <= n; i++)
		if (n % i == 0) return false;
	
	return true;
}

int main() {
	int T;
	cin >> T;
	while(T--) {
		int n;
		int p1 = 0;
		int p2 = 0;
		cin >> n;
		for (int i = 2; i * 2 <= n; i++) {
			if (isPrime(i) && isPrime(n - i)) {
				if ((p1 == 0 && p2 == 0) || (p2 - p1 > n - i - i)) {
					p1 = i;
					p2 = n - i;
				}
			}
		}
		if (p1 == 0 || p2 == 0) continue;
		cout << p1 << " " << p2 << endl;
	}
}