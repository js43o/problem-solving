#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main() {
	string s1, s2;
	cin >> s1 >> s2;

	deque<int> q;

	for (char c : s1) {
		q.push_back(c);

		if (q.size() >= s2.length()) {
			bool corrected = true;
			for (int i = 0; i < s2.length(); i++) {
				if (q[q.size() - s2.length() + i] != s2[i]) {
					corrected = false;
					break;
				}
			}

			if (corrected) for (int _ = 0; _ < s2.length(); _++) q.pop_back();
		}
	}

	if (q.empty()) cout << "FRULA";
	else for (char a : q) cout << a;
}