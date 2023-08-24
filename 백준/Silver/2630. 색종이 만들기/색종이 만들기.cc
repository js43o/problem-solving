#include <iostream>
using namespace std;

int paper[128][128];
int N;
int white;
int blue;

void recur(int x1, int y1, int x2, int y2) {
	if (x1 == x2 && y1 == y2) {
		if (paper[x1][y1] == 0) white++;
		else blue++;
		return;
	}

	bool flag = true;
	int first = paper[x1][y1];
	for (int i = x1; i <= x2; i++) {
		for (int j = y1; j <= y2; j++) {
			if (paper[i][j] != first) {
				flag = false;
				break;
			}
		}
		if (!flag) break;
	}

	int length = (x2 - x1 + 1);	// == (y2 - y1 + 1)
	int halfLength = length / 2;

	if (flag) {
		int num = length * length;
		if (first == 0) white++;
		else blue++;

		return;
	}

	recur(x1, y1, x2 - halfLength, y2 - halfLength);	// top-left
	recur(x1 + halfLength, y1, x2, y2 - halfLength);	// top-right
	recur(x1, y1 + halfLength, x2 - halfLength, y2);	// bottom-left
	recur(x1 + halfLength, y1 + halfLength, x2, y2);	// bottom-right
}

int main() {

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> paper[i][j];
		}
	}

	recur(0, 0, N - 1, N - 1);

	cout << white << '\n' << blue << '\n';
}