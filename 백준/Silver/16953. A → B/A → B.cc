#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long long A, B;
	queue<pair<long long, int>> q;

	cin >> A >> B;

	q.push({ A, 1 });

	while (!q.empty()) {
		long long a = q.front().first;
		int count = q.front().second;
		q.pop();

		if (a > B) continue;

		if (a == B) {
			cout << count << '\n';
			return 0;
		}

		q.push({ a * 2, count + 1 });
		q.push({ a * 10 + 1 , count + 1 });
	}

	cout << -1 << '\n';
}