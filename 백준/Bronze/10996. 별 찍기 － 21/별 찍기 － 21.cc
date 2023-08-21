#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	
	int count = 0;
	
	if (n == 1) {
		cout << "*";
		return 0;
	}
	
	for (int i = 0; i < n; i++) {
		int count = 0;
		while (count < n) {
			cout << "*";
			count++;
			
			if (count >= n - 1) break;
			cout << " ";
			count++;
		}
		cout << endl;
		count = 0;
		while (count < n) {
			if (count >= n - 1) break;
			cout << " ";
			count++;
			
			cout << "*";
			count++;
		}
		cout << endl;
	}
}