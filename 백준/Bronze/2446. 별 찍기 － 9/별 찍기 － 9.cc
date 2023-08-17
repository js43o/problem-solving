#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	
	int star = n * 2 - 1;
	int space = 0;
	while (star > 1) {
		for (int j = 0; j < space; j++)
			cout << " ";
		for (int i = 0; i < star; i++)
			cout << "*";
		
		star -= 2;
		space++;
		
		cout << endl;
	}
	
	while (star <= n * 2 - 1) {
		for (int j = 0; j < space; j++)
			cout << " ";
		for (int i = 0; i < star; i++)
			cout << "*";
		
		star += 2;
		space--;
		
		cout << endl;
	}
}