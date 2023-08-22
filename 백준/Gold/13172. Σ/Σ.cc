#include <iostream>
#include <vector>
using namespace std;

#define MOD 1000000007

long long cpow(long long, long long);
long long GCD(long long, long long);

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int m;
	long long result = 0;

	cin >> m;

	while (m--) {
		long long n, s;
		cin >> n >> s;
		result += (s * cpow(n, MOD - 2)) % MOD;
	}

	cout << result % MOD << endl;
}

long long GCD(long long n1, long long n2) {
	long long a = max(n1, n2);
	long long b = min(n1, n2);
	long long temp;

	while (b != 0) {
		temp = a % b;
		a = b;
		b = temp;
	}

	return a;
}

long long cpow(long long n, long long x) {
	long long res = 1;
	while (x) {
		if (x & 1) {
			res = res * n % MOD;
		}
		x = x / 2;
		n = n * n % MOD;
	}
	return res;
}