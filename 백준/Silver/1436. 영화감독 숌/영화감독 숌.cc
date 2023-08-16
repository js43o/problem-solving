#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;
	int count = 0;
	int a = 666;
	while (count < n) {
		string str = to_string(a);
		for (int i = 0; i < str.length() - 2; i++) {
			if (str.at(i) == '6' && str.at(i + 1) == '6' && str.at(i + 2) == '6') {
				count++;
				break;
			}
		}
		if (count == n) break;
		a++;
	}
	cout << a << endl;
}