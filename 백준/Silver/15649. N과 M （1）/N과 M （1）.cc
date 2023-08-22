#include <iostream>
using namespace std;

int arr[8];
bool visited[8];
int n, m;

void func(int count) {
	if (count == m) {
		for (int i = 0; i < m; i++)
			cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	
	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			visited[i] = true;
			arr[count] = i;
			func(count + 1);
			visited[i] = false;
		}
	}
}

int main() {
	cin >> n >> m;
	func(0);
}