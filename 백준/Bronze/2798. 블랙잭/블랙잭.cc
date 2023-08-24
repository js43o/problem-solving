#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	
	vector<int> cards;
	int input;
	for (int i = 0; i < n; i++) {
		cin >> input;
		cards.push_back(input);
	}
	
	int max = 0;
	for (int j = 0; j < n - 2; j++) {
		for (int k = j + 1; k < n - 1; k++) {
			for (int l = k + 1; l < n; l++) {
				int sum = cards[j] + cards[k] + cards[l];
				if (sum <= m && sum > max)
					max = sum;
			}
		}
	}
	cout << max << endl;
}