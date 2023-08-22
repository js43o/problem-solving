#include <iostream>
#include <queue>
#include <set>
using namespace std;

int N, K;
int dp[200001];
multiset<int> result;

int main() {
	cin >> N >> K;

	queue<pair<int, int>> q;	// (위치, 시간)
	q.push({ N, 0 });
	
	while (!q.empty()) {
		int v = q.front().first;
		int t = q.front().second;
		q.pop();

		if (v == K) {
			result.insert(t);
			continue;
		}

		int dvs[3] = { v - 1, v + 1, v * 2 };
		for (int dv : dvs) {
			if (dv != N && dv >= 0 && dv <= 100000) {
				if (dp[dv] != 0 && t + 1 > dp[dv]) continue;	// 이미 방문한 곳보다 현재 시간이 더 늦다면 방문 안함

				dp[dv] = t + 1;
				q.push({ dv, t + 1 });
			}
		}
	}

	int counts = 0;
	int minT = *(result.begin());
	for (int t : result) {
		if (t == minT) counts++;
		if (t > minT) break;
	}

	cout << dp[K] << '\n' << counts << '\n';
} 