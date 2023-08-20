#include <iostream>
using namespace std;

int main() {
	int input;
	int score[5];
	for (int i = 0; i < 5; i++) {
		cin >> input;
		if (input < 40) input = 40;
		score[i] = input;
	}
	int m;
	for (int i = 0; i < 5; i++) {
		m += score[i];
	}
	cout << m / 5 << endl;
}