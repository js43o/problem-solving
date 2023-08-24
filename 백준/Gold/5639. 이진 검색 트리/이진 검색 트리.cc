#include <iostream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> tree;

void postOrder(int start, int end) {
	if (start >= end) {
		return;
	}
	int idx = start + 1;
	while (idx < end) {
		if (tree[idx] > tree[start]) {
			break;
		}
		idx++;
	}

	postOrder(start + 1, idx);
	postOrder(idx, end);
	cout << tree[start] << '\n';
}

int main() {
	while (1) {
		string line;
		getline(cin, line);

		if (line.empty()) break;

		tree.push_back(stoi(line));
	}

	postOrder(0, tree.size());
}