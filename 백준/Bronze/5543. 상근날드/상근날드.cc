#include <iostream>
using namespace std;

int main() {
	int ham[3] = {};
	int drk[2] = {};
	
	cin >> ham[0] >> ham[1] >> ham[2];
	cin >> drk[0] >> drk[1];
	
	int set[6] = {};
	int idx = 0;
	
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			set[idx] = ham[i] + drk[j] - 50;
			idx++;
		}
	}
	
	int cheap = set[0];
	for (int k = 1; k < 6; k++) {
		if (cheap > set[k])
			cheap = set[k];
	}
	cout << cheap;
}