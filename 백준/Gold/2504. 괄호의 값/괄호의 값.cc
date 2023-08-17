#include <iostream>
#include <stack>
#include <string>
using namespace std;

// https://thegloryofgod.tistory.com/82

int main() {
	stack<string> s;
	string input, cur;
	cin >> input;
	int sum, result = 1;

	for (int i = 0; i < input.length(); i++) {
		cur = input.at(i);

		if (cur == "(" || cur == "[") {
			s.push(cur);
		}
		else {
			sum = 1;

			while (!s.empty() && s.top() != "(" && s.top() != "[") {
				sum *= stoi(s.top());
				s.pop();
			}

			if (s.empty() || (cur == ")" && s.top() != "(") || (cur == "]" && s.top() != "[")) {
				result = 0;
				break;
			}

			if (cur == ")")
				sum *= 2;
			else
				sum *= 3;
			s.pop();

			while (!s.empty() && s.top() != "(" && s.top() != "[") {
				sum += stoi(s.top());
				s.pop();
			}

			s.push(to_string(sum));
		}
	}

	if (result == 0 || s.size() != 1 || s.top() == "[" || s.top() == "(")
		cout << 0 << endl;
	else
		cout << s.top() << endl;

	return 0;
}
