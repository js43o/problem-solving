#include <iostream>
#define MAX 15
using namespace std;

int n;
int sol = 0;
bool* arr;
bool* sum;
bool* dif;

void queen(int count) {
	if (count == n) {
		sol++;
		return;
	}
	
	for (int i = 0; i < n; i++) {
		if (!arr[i] && !sum[count + i] && !dif[count - i + n - 1]) {
			arr[i] = true;
			sum[count + i] = true;
			dif[count - i + n - 1] = true;
			
			queen(count + 1);
			
			arr[i] = false;
			sum[count + i] = false;
			dif[count - i + n - 1] = false;
		}
	}
	
	return;
}

int main() {
	cin >> n;
	
	arr = new bool[n];
	sum = new bool[n * 2 - 1];
	dif = new bool[n * 2 - 1];
	
	// 1행 시행. i는 열 (1행부터 n행까지)
	for (int i = 0; i < n; i++) {
		arr[i] = true;
		sum[0 + i] = true;
		dif[0 - i + n - 1] = true;
		
		queen(1);	// 2행부터 시행.
		
		arr[i] = false;
		sum[0 + i] = false;
		dif[0 - i + n - 1] = false;
	}
	
	delete[] arr;
	delete[] sum;
	delete[] dif;
	
	cout << sol << endl;
}