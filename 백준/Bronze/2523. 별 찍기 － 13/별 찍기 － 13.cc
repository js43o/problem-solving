#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	
	int count = 1;
	while (count < n) {
		for (int i = 0; i < count; i++)
			cout << "*";
		cout << endl;
		count++;
	}
	while (count > 0) {
		for (int i = 0; i < count; i++)
			cout << "*";
		cout << endl;
		count--;
	}
}