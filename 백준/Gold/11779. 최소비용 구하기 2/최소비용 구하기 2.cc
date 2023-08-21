#include <iostream>
#include <vector>
#include <queue>
#include <set>
#define INF 1e9
using namespace std;

int N, M, a, b, r, start, finish;
vector<pair<int, int>> city[1001];
int dist[1001];
int parent[1001];

int main() {
	for (int i = 0; i < 1001; i++) {
		dist[i] = INF;
	}

	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		cin >> a >> b >> r;
		city[a].push_back({ b, r });
	}

	cin >> start >> finish;

	priority_queue<pair<int, int>> pq;
	dist[start] = 0;
	pq.push({ 0, start});

	while (!pq.empty()) {
		auto v = pq.top();	pq.pop();
		int cur = v.second;

		if (cur == finish) break;

		for (auto bus : city[cur]) {
			int to = bus.first;
			int w = bus.second;

			if (dist[cur] + w < dist[to]) {
				dist[to] = dist[cur] + w;
				pq.push({ -dist[to], to });
				parent[to] = cur;
			}
		}
	}

	cout << dist[finish] << '\n';

	int cur = finish;
	deque<int> way = { cur };

	while (cur != start) {
		cur = parent[cur];
		way.push_front(cur);
	}

	cout << way.size() << '\n';

	for (int v : way) {
		cout << v << " ";
	}
	cout << '\n';
}