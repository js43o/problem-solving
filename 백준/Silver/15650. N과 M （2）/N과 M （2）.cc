#include <iostream>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];
bool visited[MAX];

void func(int count) {
	if (count == m) {
		for (int i = 0; i < m; i++)
			cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	
	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			if (count > 0 && arr[count - 1] > i) continue;
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