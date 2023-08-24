#include <iostream>
using namespace std;

char stars[2187][2187];

void point(int x, int y, int n) {
	if (n == 1) {
		stars[x][y] = '*';
	}
	else {
		point(x, y, n / 3);
		point(x + n / 3, y, n / 3);
		point(x + n * 2 / 3, y, n / 3);
		
		point(x, y + n / 3, n / 3);
		// point(x + n / 3, y + n / 3, n / 3);
		point(x + n * 2 / 3, y + n / 3, n / 3);
		
		point(x, y + n * 2 / 3, n / 3);
		point(x + n / 3, y + n * 2 / 3, n / 3);
		point(x + n * 2 / 3, y + n * 2 / 3, n / 3);
	}
}

int main() {
	int input;
	cin >> input;

	for (int i = 0; i < input; i++) {
		for (int j = 0; j < input; j++) {
			stars[i][j] = ' ';
		}
	}
	
	point(0, 0, input);
	
	for (int i = 0; i < input; i++) {
		for (int j = 0; j < input; j++) {
			cout << stars[i][j];
		}
		cout << endl;
	}
}