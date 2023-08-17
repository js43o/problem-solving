#include <iostream>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

bool arr[10000][10000];

struct pos {
	int y;
	int x;
};

void draw(pos parent, int n) {
	if (n == 3) {
		arr[parent.y][parent.x] = true;
		arr[parent.y + 1][parent.x - 1] = true;
		arr[parent.y + 1][parent.x + 1] = true;

		arr[parent.y + 2][parent.x - 2] = true;
		arr[parent.y + 2][parent.x - 1] = true;
		arr[parent.y + 2][parent.x] = true;
		arr[parent.y + 2][parent.x + 1] = true;
		arr[parent.y + 2][parent.x + 2] = true;

		return;
	}

	pos leftChild = { parent.y + n / 2, parent.x - n / 2 };
	pos rightChild = { parent.y + n / 2, parent.x + n / 2 };

	draw(parent, n / 2);
	draw(leftChild, n / 2);
	draw(rightChild, n / 2);
}

int main() {
	int N;

	cin >> N;

	draw({ 0, N }, N);

	for (int i = 0; i < N; i++) {
		for (int j = 1; j < N * 2; j++) {
			if (arr[i][j]) cout << "*";
			else cout << " ";
		}
		cout << '\n';
	}
}