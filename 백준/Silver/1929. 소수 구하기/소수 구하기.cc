#include <iostream>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	bool* arr = new bool[m + 1];
	
	arr[0] = false;
	arr[1] = false;
	
	for (int i = 2; i <= m; i++)
		arr[i] = true;
	
	for (int i = 2; i * i <= m; i++) {
		if (arr[i] == false) continue;
		for (int j = 2; i * j <= m; j++)
			arr[i * j] = false;
	}
	
	for (int i = n; i <= m; i++)
		if (arr[i] == true) cout << i << "\n";
}