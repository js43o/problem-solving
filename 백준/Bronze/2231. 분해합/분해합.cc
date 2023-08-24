#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;
	int result = n;
	for (int i = 0; i < n; i++) {
		string str = to_string(i);
		int sum = i;
		for (int j = 0; j < str.length(); j++)
			sum += str[j] - '0';
		
		if (sum == n && i <= result)
			result = i;
	}
	if (result == n) cout << 0 << endl;
	else cout << result << endl;
}