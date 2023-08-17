#include <iostream>
using namespace std;

// 거품 정렬
int main() {
	int n;
	cin >> n;
	int* arr = new int[n];
	
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	
	for (int i = n; i > 0; i--) {
		for (int j = 1; j < i; j++) {
			if (arr[j] < arr[j - 1]) {
				int temp = arr[j - 1];
				arr[j - 1] = arr[j];
				arr[j] = temp;
			}
		}
	}
	
	for (int i = 0; i < n; i++)
		cout << arr[i] << "\n";
}