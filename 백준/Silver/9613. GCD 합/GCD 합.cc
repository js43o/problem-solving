#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

int gcd(int n1, int n2) {
	int a = max(n1, n2);
	int b = min(n1, n2);

	int res = -1;

	while (res) {
		res = a % b;
		a = b;
		b = res;
	}

	return a;
}

int main()
{
	int T;
	cin >> T;

	while (T--) {
		int n, input;
		vector<int> vec;

		cin >> n;

		for (int i = 0; i < n; i++) {
			cin >> input;
			vec.push_back(input);
		}

		if (n == 1) {
			cout << input << endl;
			continue;
		}

		long long result = 0;

		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1;  j < n; j++) {
				result += gcd(vec[i], vec[j]);
			}
		}

		cout << result << endl;
	}
}