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
	int n;
	while(cin >> n) {
		if (n == 0) return 0;
		int count = 0;
		for (int i = n + 1; i <= 2 * n; i++)
			if (isPrime(i)) count++;
		
		cout << count << endl;
	}
}