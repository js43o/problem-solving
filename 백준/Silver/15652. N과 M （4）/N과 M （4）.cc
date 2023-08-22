#include <iostream>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];

void func(int count) {
	if (count == m) {
		for (int i = 0; i < m; i++)
			cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	
	for (int i = 1; i <= n; i++) {
		if (arr[count - 1] > i) continue;
		arr[count] = i;
		func(count + 1);
	}
}

int main() {
	cin >> n >> m;
	func(0);
}