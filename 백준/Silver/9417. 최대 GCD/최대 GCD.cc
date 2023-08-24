#include <iostream>
#include <vector>
#include <string>
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
	cin.ignore();

	while (T--) {
		string input;
		vector<int> vec;

		getline(cin, input);
		string temp = "";

		for (int i = 0; i < input.length(); i++) {
			if (input[i] == ' ') {
				vec.push_back(stoi(temp));
				temp = "";
			}
			else {
				temp += input[i];
			}
		}
		vec.push_back(stoi(temp));


		if (vec.size() == 1) {
			cout << vec[0] << endl;
			continue;
		}

		int result = 0;

		for (int i = 0; i < vec.size(); i++) {
			for (int j = i + 1;  j < vec.size(); j++) {
				result = max(result, gcd(vec[i], vec[j]));
			}
		}

		cout << result << endl;
	}
}